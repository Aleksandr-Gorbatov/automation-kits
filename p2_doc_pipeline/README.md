# Doc-Pipeline — free tier: Email → Claude extraction → Google Sheet

Orders, invoices and requests arrive as email. Someone retypes them into a
spreadsheet by hand. This n8n workflow does it instead:

1. **IMAP trigger** watches the mailbox
2. **Claude** extracts structured fields (company, document type & number,
   date, amount, currency, items summary)
3. Clean rows are **appended to a Google Sheet**
4. Anything the model could not parse lands on a separate **exceptions
   sheet** with the error — nothing is lost silently

## Setup (~15 minutes)

1. Import `email_extract_to_sheet.json` into n8n (Workflows → Import from file).
2. Create **IMAP credentials** for the mailbox and select them in the trigger node.
3. Set `ANTHROPIC_API_KEY` as an environment variable on your n8n instance
   (get a key at console.anthropic.com).
4. In both Google Sheets nodes pick your spreadsheet and sheets
   (one for clean rows, one for exceptions).
5. Activate. Send yourself a test invoice.

Tune the field list by editing the prompt inside the
"Claude: extract fields" node — it's plain text, add or remove fields freely.

**Free-tier limitation:** this workflow does not dedupe. If the trigger fires twice
(IMAP retry, workflow restart), you get duplicate rows in the sheet. The full kit
adds idempotent execution — every email processed exactly once.

## What the full kit adds ($29)

| Free tier | Full kit |
|---|---|
| Extraction to Google Sheet | everything on the left, plus: |
| | **docx/Excel generation** — a formatted document per email, from your template |
| | **Prompt template pack**: invoices, orders, requests (tested field schemas) |
| | **File routing** — finished documents filed to Drive/folder structure |
| | **Idempotency** — runs twice, nobody gets duplicated |
| | 20-minute setup guide for the whole chain |

**Full kit — early access:** the packaged version ships this week. Email
a.gorbatov80@gmail.com with subject "Doc-Pipeline full kit" and you get it first,
at the launch price ($29, USDT).

Questions or a custom pipeline? → a.gorbatov80@gmail.com

MIT license for the free tier.
