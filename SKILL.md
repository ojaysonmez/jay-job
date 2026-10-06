---
name: "jay-job"
description: "Triage a pasted LinkedIn job posting for Jay Sonmez: red and yellow flags, features line, fit verdict, and a tailored short cover letter. Use whenever Jay shares a job description or posting file."
---

# Job posting triage

Jay is a product and project management candidate. He shares postings, often as a LinkedIn search page .txt export with one focused posting inside. Read only the focused posting, ignore the surrounding search results, and reply in the order below.

## Reply order

1. Red and yellow flags, each as a big markdown heading, before anything else.
2. The job features line.
3. A fit verdict of two to four sentences.
4. A short cover letter, unless there is a red flag, in which case give a one-line skip recommendation and no letter.

If Jay only asks "did we apply to this before", answer that first, then continue with the same order.

## Flags

Red flag, heading starts with ❌, for hard disqualifiers:
- Wrong domain or function (for example sales, pure engineering, design).
- Required domain experience Jay does not have (for example DICOM, security, fintech-only, logistics, payments, GRC).
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

Not flags, so never warn about them:
- Location, remote status, on-site or hybrid, state restrictions, California exclusions. Jay applies out of state, including on-site and hybrid roles. Show these only in the features line.
- Low pay. Show it only in the features line.

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
- If the reply recommends skipping (a red flag), set the new row's status to skipped. Jay sometimes applies anyway, so when he says he applied, change the status to applied and recount that company's roles.
- To add many saved posting files at once, run `python3 scripts/build_seen_jobs.py POSTINGS_DIR references/seen-jobs.csv`. The script reads LinkedIn exports and Wellfound lists, skips files already in the CSV, keeps existing status values, recomputes the role counts, and prints the files it could not read. For each file it prints, open the file, find the company, title, and location, and append a row by hand with source Career site.

## Features line

One compact line of facts, using only the items that apply: 💰 pay, 🏠 remote status, 📍 location or in-person days, 👥 applicant counts, 🤝 connections (give the names shown), 📈 company growth, 🏢 company type or size, 🎯 level, 🎓 education, 🏥 health domain, 🧩 anything else notable, 📄 contract, ✈️ travel, 🛂 visa, ⚡ Easy Apply.

## Fit verdict

Use strong, good, moderate, low, or skip. Name the two or three facts from Jay's background that match and the main gap. Be honest about gaps.

## What Jay can claim

Only use these facts, and never invent others:
- Software engineer at The New York Times (2008 to 2010) and The Wall Street Journal (2011 to 2012).
- UI product analytics at Walmart eCommerce on ASDA Groceries, using SQL dashboards and drop-off analysis.
- UI product work at PwC Advisory on an enterprise financial reporting product with 10+ Scrum teams, Tableau and Power BI integrations, and secure dashboards.
- Co-founded Talent Envoy, an AI-assisted recruiting workflow platform, from zero to one with a human in the loop.
- Ran a recruiting agency.
- Founder in health technology: an FDA-regulated diagnostic paired with clinical decision support software, a semiconductor supplier for the analog front end, and 13+ contract manufacturers evaluated.
- A CMS-sourced remote patient monitoring reimbursement model and a five-year business case for clinicians, payers, and employers.
- A market-sizing analysis of about 24 million US adults using NHANES data, run and verified by Jay.
- An NIH SBIR application written in three weeks with one scientist.
- Electrical Engineering degree, Hacettepe University.
- Daily use of Claude and Claude Code, with every output verified by Jay.
- Strong SQL.
- Jira, used for backlog grooming, sprint boards, and writing tickets. Do not tie it to a specific employer unless Jay says which.
- Python at a basic level. Say "some Python" or "basic Python", never present it as a core skill.

Do not claim anything outside that list. In particular, do not claim A/B testing or experimentation, Figma, Confluence, Rally, Aha, Azure DevOps, R, payments or fintech, FHIR or EHR integration, security, a clinical license, education or government experience, or a formal product owner or product manager title with several years of tenure.

## Cover letter rules

- Show it in chat only, with no heads-up line before it and no notes around it.
- Short: about 120 to 170 words, three short paragraphs.
- Humanized: it should read as written by Jay, plain and specific, not like AI output.
- Complete sentences only. No fragments, no broken lists.
- No em dashes anywhere.
- Describe the founder experience as "as a founder in health technology". Do not name his companies.
- Match tone to the role. Entry-level or low-profile roles get a modest, eager tone. Mid-level roles can be more confident.
- Mention one concrete detail from the posting so it is clearly written for this role.
- Only resume-true claims from the list above.

### Template

Dear [Hiring Manager name, or "Hiring Team"],

I am applying for the [role title] position at [company]. [One sentence on why this role or the company's product interests Jay, using a real detail from the posting.]

[One or two sentences linking the closest two matches from the claimable list to what the posting asks for. Add one sentence naming how Jay works, such as writing clear user stories, using SQL to check a hunch, or verifying every AI-assisted output.]

[One sentence on what Jay would bring or learn in the first months. Close with thanks and an invitation to talk.]

Sincerely,
Jay Sonmez

## Form answers

When Jay pastes application form questions, reply with only the paste-ready answers, in the same writing style as the cover letter, with no notes, caveats, or placeholders.

## Name

The candidate name is Jay Sonmez everywhere.

## Documents

If any document is requested, produce DOCX, never PDF.