# <<Paper title>>: glossary

## How to use

- This glossary is the only authority for wording in this paper. The writer and the reviser write by it, and drafts are checked against it.
- Before writing each section, scan its outline and check every proper name, every recurring term and every word easily confused in the field against this glossary (default constraints W1).
- Each entry has one of three statuses:
  - confirmed: decided by the user, or given in English by the outline; use it as it is;
  - pending: has a suggested form the user has not reviewed yet; ask the user before writing;
  - to check: unclear; look for evidence in papers first, then ask the user with the candidate forms.
- Register entries by concept, not by surface form. When one word of the outline stands for different concepts, split it into several entries.
- Once the user confirms an entry, record who confirmed it, the date and the basis under "Confirmed by / basis". When the user later corrects an entry, change it here and add a line to the change log at the end.
- "Outline location" gives the section and the outline line, for example "Introduction L9"; line numbers refer to outline.md in that section's work folder.
- When a forbidden form changes, change "forbidden" in check_rules.json too.

## Proper names (names the outline already gives in English; copy them)

Names of the method, its components, the challenges and the like. The outline already gives them in English; write them exactly as given, without rewording or abbreviating. IDs start at N01, with two digits, to keep them apart from rule IDs. The check script reads the names from the English column of this table, so:

- The English column holds names only. Put the full name and the short form in the same cell, separated by " / ", for example Cross-Lingual Retrieval / CLR.
- Notes, such as the meaning or when to use the full name and when the short form, go in the Notes column.
- The heading of this section must contain "Proper names" and the column must be named "English"; the script finds the table by these two.

| ID | Outline term | English | Notes | Status | Confirmed by / basis |
|---|---|---|---|---|---|
| N01 | <<form in the outline>> | <<full name / short form>> | <<usage notes>> | <<status>> | <<who, date, basis>> |

## Terms (words whose English form has to be chosen)

Ordinary terms and concepts in the outline whose English form has to be decided, for example whether a word is written decision or classification. Unlike proper names, terms may have allowed variants and forbidden forms; when one word of the outline stands for different concepts, it becomes several entries. IDs start at T01, with two digits, to keep them apart from rules T1 to T3.

| ID | Outline term (location) | Concept | English | Allowed variants | Forbidden forms | Keep apart from | Status | Confirmed by / basis |
|---|---|---|---|---|---|---|---|---|
| T01 | <<form in the outline (Introduction L9)>> | <<one sentence on what this entry means>> | <<chosen form>> | <<forms that may be used instead>> | <<forms that must not appear>> | <<IDs of easily confused entries>> | <<status>> | <<who, date, basis>> |

The Concept column tells apart the entries that share one outline word; "Keep apart from" lists the IDs of entries easily confused with this one.

## Change log

- <<date>>: which entry changed and why.
