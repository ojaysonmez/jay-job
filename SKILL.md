---
name: "jay-job"
description: "Triage a pasted LinkedIn job posting for Jay: red and yellow flags, features line, fit verdict, and a tailored short cover letter. Use whenever Jay shares a job description or posting file."
---

# Job posting triage

Jay shares postings, often as a LinkedIn search page .txt export with one focused posting inside. Read only the focused posting, ignore the surrounding search results, and reply in the order below.

## Reply order

1. Red and yellow flags, each as a big markdown heading, before anything else.
2. The job features line.
3. A fit verdict of two to four sentences.
4. A short cover letter, unless there is a red flag, in which case give a one-line skip recommendation and no letter.

If Jay only asks "did we apply to this before", answer that first, then continue with the same order.

## Flags

Red flag, heading starts with ❌, for hard disqualifiers:
- Wrong domain or function (for example sales, pure engineering, design).
- Required domain experience Jay does not have (see the domain list in `references/profile.md`).
- A required language Jay does not speak.
- Suspected career-services scams posing as employers (a firm selling coaching or placement under a job title).

Yellow flag, heading starts with ⚠️, for lesser warnings:
- Possible duplicate of a posting already reviewed (see the seen jobs list below).
- Other roles at the same company (see the multiple roles rule below).
- Thin posting with little description.
- Staffing firm or contract role.
- Stale posting (older than about a month, compared with today's date).
- Requirements mismatch (years of experience, specific tools, titles).
- Reposted listing.
- 100 or more applicants or clicks.
- Application happens off LinkedIn.
- Description actually cut off. A trailing "... more" label alone is not truncation.

Not flags, so never warn about them: everything listed under "Not flags" in `references/profile.md`. Show those items only in the features line.

## Seen jobs list

The list of every posting Jay has shared lives in `references/seen-jobs.csv`, next to this file. It is private, so it must be listed in `.gitignore` and never committed. Columns: company, position, location, pay, source, roles_at_company, other_roles_at_company, file, status. The status column is filled by Jay or by you (applied, skipped, or blank).

### Duplicate check

1. Before writing the reply, read `references/seen-jobs.csv` if it exists. Match the company name loosely (ignore case, Inc, LLC, punctuation) and the title loosely, since the same role is often reposted under another location or wording.
2. If the same company and role is already listed, say so under a ⚠️ heading, with its status. If the status is applied, say Jay already applied.
3. If the file does not exist, check the current conversation and any memory available, and say which sources you could check.

### Multiple roles at one company

Jay is happy to apply to two roles at one company, but not three or more.
- If the company already has one other role in the list, add a short ⚠️ heading naming that role, and note that applying to both is fine.
- If the company already has two or more other roles, add a ⚠️ heading listing them and recommend applying to at most two in total. Say which two fit best, including the new one.
- Roles whose status is skipped do not count. The script already leaves them out of `roles_at_company` and `other_roles_at_company`. When you add or edit a row by hand, recount the same way and do not trust a stored number that may be out of date.

### Keeping the list current

- Show the full reply (flags, features line, verdict, cover letter) first. The reply must be the last thing in the turn, with no tool call after it, because the app folds away any text that comes before a tool call. Save the row later: at the start of the next turn, before anything else, append one row to the CSV for the posting just triaged (company, position, location, pay, source, file name, blank status), then update the roles_at_company and other_roles_at_company columns for that company. Reading the CSV for the duplicate check still happens before the reply. Skip the append if the posting is already in the list.
- When Jay says he applied to or skipped a role, set its status.
- If the reply recommends skipping (a red flag), set the new row's status to skipped. When he says he applied, change the status to applied and recount that company's roles.
- To add many saved posting files at once, run `python3 scripts/build_seen_jobs.py POSTINGS_DIR references/seen-jobs.csv`. The script reads LinkedIn exports and Wellfound lists, skips files already in the CSV, keeps existing status values, recomputes the role counts, and prints the files it could not read. For each file it prints, open the file, find the company, title, and location, and append a row by hand with source Career site.

## Features line

One compact line of facts, using only the items that apply: 💰 pay, 🏠 remote status, 📍 location or in-person days, 👥 applicant counts, 🤝 connections (give the names shown), 📈 company growth, 🏢 company type or size, 🎯 level, 🎓 education, 🏥 health domain, 🧩 anything else notable, 📄 contract, ✈️ travel, 🛂 visa, ⚡ Easy Apply.

## Fit verdict

Use strong, good, moderate, low, or skip. Name the two or three facts from Jay's background that match and the main gap. Be honest about gaps.

## What Jay can claim

The list lives in `references/profile.md`, next to this file. It is private, so it is listed in `.gitignore` and must never be committed or copied into this file. Read it before writing a verdict or a letter, use only the facts in it, and never invent others. If the file does not exist, ask Jay for his background before writing a letter.

Do not claim anything outside that list. The profile file also has a "Never claim" list; follow it.

## Cover letter rules

- Show it in chat only, with no heads-up line before it and no notes around it.
- Short: about 120 to 170 words, three short paragraphs.
- Plain and specific, in Jay's own voice.
- Complete sentences only. No fragments, no broken lists.
- No em dashes anywhere.
- Describe the founder experience as "as a founder in health technology". Do not name his companies.
- Match tone to the role, following the tone notes in `references/profile.md`.
- Mention one concrete detail from the posting so it is clearly written for this role.
- Only resume-true claims from the list above.

### Template

Dear [Hiring Manager name, or "Hiring Team"],

I am applying for the [role title] position at [company]. [One sentence on why this role or the company's product interests Jay, using a real detail from the posting.]

[One or two sentences linking the closest two matches from the claimable list to what the posting asks for. Add one sentence naming how Jay works, such as writing clear user stories, using SQL to check a hunch, or verifying every AI-assisted output.]

[One sentence on what Jay would bring or learn in the first months. Close with thanks and an invitation to talk.]

Sincerely,
[Full name from `references/profile.md`]

## Form answers

When Jay pastes application form questions, reply with only the paste-ready answers, in the same writing style as the cover letter, with no notes, caveats, or placeholders.

## Name

Use the full name from `references/profile.md` everywhere a name is needed. Never write it into this file.

## Documents

If any document is requested, produce DOCX, never PDF.