#!/usr/bin/env python3
"""Build or update references/seen-jobs.csv from saved posting .txt files.

Usage: python3 scripts/build_seen_jobs.py POSTINGS_DIR references/seen-jobs.csv

- Parses LinkedIn exports (focused posting), Wellfound lists, and LinkedIn
  "Save <title> at <company>" pages.
- Skips files already listed in the CSV's `file` column, so it is safe to rerun.
- Keeps any `status` values you typed (applied, skipped, ...).
- Prints files it could not parse so you can add them by hand.
"""
import csv, glob, os, re, sys, collections

COLS = ["company", "position", "location", "pay", "source",
        "roles_at_company", "other_roles_at_company", "file", "status"]

def lines(path):
    return [l.strip() for l in open(path, errors="ignore").read().split("\n")]

def norm_company(c):
    c = re.sub(r"\b(inc|llc|ltd|corp|corporation|co)\b\.?", "", c.lower())
    return re.sub(r"[^a-z0-9]+", " ", c).strip()

def norm_title(t):
    return re.sub(r"\W+", " ", t.lower()).strip()

def parse(path):
    L = lines(path); txt = "\n".join(L); out = []
    if "Company logo for" in txt:                       # LinkedIn, main layout
        for i, l in enumerate(L):
            m = re.match(r"Company logo for, (.+)\.$", l)
            if m:
                rest = [x for x in L[i + 1:i + 12] if x]
                if len(rest) >= 3:
                    out.append((m.group(1), rest[1], rest[2].split(" · ")[0], "", "LinkedIn"))
                break
    elif "Wellfound" in txt:                            # Wellfound job lists
        comp = ""
        for i, l in enumerate(L):
            m = re.match(r"^(.+) company logo$", l)
            if m:
                nxt = [x for x in L[i + 1:i + 4] if x]
                comp = nxt[0] if nxt else m.group(1)
            if l.startswith("Posted ") and i + 1 < len(L) and L[i + 1] == "Save":
                j = i - 1
                if L[j] == "Recruiter recently active": j -= 1
                loc, title = L[j], L[j - 1]
                pay = ""
                m2 = re.search(r"((?:[$£₹]\d[\d,.]*k?\s*–\s*[$£₹]\d[\d,.]*k?).*)$", loc)
                if m2: pay, loc = m2.group(1), loc[:m2.start()]
                out.append((comp, title, loc, pay, "Wellfound"))
    else:                                               # LinkedIn, alternate layout
        for l in L:
            m = re.match(r"^Save (.+?)\s+at (.+)$", l)
            if m:
                out.append((m.group(2), m.group(1), "", "", "LinkedIn")); break
    return [(c.strip(), re.sub(r"\s+", " ", t).strip(), loc.strip(), pay, src)
            for c, t, loc, pay, src in out if c and t]

def main(src_dir, csv_path):
    rows = []
    if os.path.exists(csv_path):
        rows = list(csv.DictReader(open(csv_path)))
    known_files = {f for r in rows for f in r["file"].split("; ")}
    seen = {(norm_company(r["company"]), norm_title(r["position"])): r for r in rows}
    unparsed = []
    for p in sorted(glob.glob(os.path.join(src_dir, "*.txt"))):
        name = os.path.basename(p)
        if name in known_files: continue
        found = parse(p)
        if not found: unparsed.append(name); continue
        for c, t, loc, pay, src in found:
            k = (norm_company(c), norm_title(t))
            if k in seen:
                if name not in seen[k]["file"]: seen[k]["file"] += "; " + name
                continue
            r = dict(company=c, position=t, location=loc, pay=pay, source=src,
                     roles_at_company="", other_roles_at_company="", file=name, status="")
            seen[k] = r; rows.append(r)
    by = collections.defaultdict(list)
    for r in rows: by[norm_company(r["company"])].append(r["position"])
    for r in rows:
        group = by[norm_company(r["company"])]
        r["roles_at_company"] = len(group)
        r["other_roles_at_company"] = " | ".join(t for t in group if t != r["position"])
    rows.sort(key=lambda r: (norm_company(r["company"]), r["position"].lower()))
    with open(csv_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLS); w.writeheader(); w.writerows(rows)
    print(f"{len(rows)} jobs, {len(by)} companies")
    if unparsed:
        print("Could not parse (add by hand):")
        for u in unparsed: print("  ", u)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
