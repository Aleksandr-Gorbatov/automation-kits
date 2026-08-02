# Telegram Site-Report Bot — field reports without forms

Your field crew texts like they always do — the bot builds the report.

A foreman forwards three photos and two lines of text. The bot logs a
structured entry: **site, work type, quantity, photo evidence** — and the
office gets a clean daily summary instead of a scroll of chat messages.

The trick: no 8-field forms, no buttons-and-menus quiz. **AI mapping**
(Claude) reads free text the way a human dispatcher would, and fills the
structure itself. Crews don't change how they write; the data still comes
out structured.

The core pipeline (photo intake, SQLite log, report summaries) is battle-tested on a
live construction site — an 1,100-student school build, daily reports from 4 crews.
The packaged English kit is the same skeleton with an English vocabulary layer.

## Try the demo

**Demo bot:** launching shortly — email me and I'll ping you the day it's live.
You'll send it a message like `poured concrete 3rd floor section B, 12 cubic meters`
+ a photo and get back the structured entry. Limited to 5 reports/day.

## What's in the full kit ($39)

- Python source (aiogram 3) — deploy on any VPS in an evening
- Claude-powered free-text mapping with a **pluggable vocabulary**:
  tune site names, work types and units to your trade in one file
- SQLite log + daily/weekly Excel summary generation
- Photo handling: originals stored, entries link to them
- Deploy guide: systemd service, token setup, backup

**Early access:** the English kit is being finalized. Email a.gorbatov80@gmail.com
with subject "Site-Report Bot — early access" — you get it first, at the launch
price ($39, USDT).

Need it adapted — different language, different trade, CRM integration?
Custom work is available: a.gorbatov80@gmail.com
