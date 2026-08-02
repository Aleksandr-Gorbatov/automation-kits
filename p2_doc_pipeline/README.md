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

**Get the full kit:** https://nowpayments.io/payment/?iid=4648946085 ($29, USDT) ·
[all kits & how buying works](https://automation-kits.pages.dev/c/gh).
Delivery by email within 24 hours of payment (usually much sooner). Nothing after
24h? Email me the payment ID: immediate delivery or a full refund.

Questions or a custom pipeline? → a.gorbatov80@gmail.com

## FAQ

**Why USDT and not a card?** Card checkout isn't available to me yet — the invoice
page walks you through paying from any wallet or exchange. You always have my email
and a receipt; the refund policy above applies either way.

**Which n8n versions?** Built and tested on current n8n (1.x). Uses only standard
nodes (IMAP, HTTP Request, Google Sheets/Docs/Drive) — no community nodes to install.

**Can I use a different model or provider?** The extraction step is one HTTP node
with a plain-text prompt — pointing it at another provider is a URL + header change.
The prompt pack is written for Claude but readable by anything.

**My documents are not in English — will extraction work?** Yes; the model handles
mixed-language mail well. Add one line to the prompt naming your languages and
currencies for best results.

MIT license for the free tier.

## Changelog

- **2026-08-01** — v1.0: first public release (free tier: IMAP → Claude extraction →
  Google Sheet with an exceptions sheet; full kit: docx generation, template pack,
  Drive filing, idempotency).
- **2026-08-02** — README: FAQ, changelog, storefront link.
