# Telegram Site-Report Bot — your daily log builds itself

Your crew already texts you what got done. The bot turns those messages into
a real site record.

A foreman forwards three photos and two lines of text. The bot logs a dated,
job-tagged entry: **job, work item, quantity, photo evidence** — and the
office gets a clean daily log instead of a scroll of chat messages nobody
can prove anything with.

The trick: no forms, no app for the crew to learn. **AI mapping** (Claude)
reads free text the way a dispatcher would and fills the structure itself.
The crew doesn't change how they write; the record still comes out structured
and timestamped.

The core pipeline (photo intake, SQLite log, summaries) is battle-tested on a
live construction site — an 1,100-student school build, daily reports from 4
crews. The packaged English kit is the same skeleton with an English trade
vocabulary layer.

## What your reports feed into

The bot doesn't print contract forms. It builds the **contemporaneous
record** those forms — and those arguments — depend on: dated, structured,
photo-backed entries per job per day.

**US / Canada**
- **Daily log** — the entry itself is your daily log: date, job, work
  performed, quantities, photos. The document GC specs demand and dispute
  lawyers ask for first.
- **Pay applications (AIA G702/G703)** — your % complete is only as
  defensible as the daily backup behind it. Day-by-day evidence of what was
  installed, and when, to bill against.
- **T&M / extra work tickets** — who, what, when, photos: captured the same
  day, ready to put in front of the GC's rep for signature before the crew
  leaves site.
- **Mechanic's / builder's lien** — deadlines run from the last date labor
  or material was furnished. With every crew text logged, that date is a
  query, not a guess.

**UK / Ireland**
- **Site diary** — a running, dated diary per job, built from texts the crew
  already sends, not reconstructed from memory at 9pm.
- **Dayworks sheets, variations, EOT claims** — all live or die on
  contemporaneous evidence; this is where that evidence accumulates daily.

**Australia / NZ**
- **Progress claims (Security of Payment Acts)** — in adjudication, the
  party with the better dated record of work-done-by-date usually wins.

**Germany / Austria / Switzerland**
- **Bautagebuch** (a VOB/B contract duty) — daily crew messages roll up into
  it instead of being reconstructed on Friday. **Rapportzettel / Regiebericht**
  — same-day basis for a signable ticket, so Regie hours stop being written
  off. (German vocabulary layer: planned — email me if you need it.)

**What the bot deliberately does not do:** generate AIA G702/G703, statutory
payment claim forms, or signed documents. It produces the dated, structured
raw material your office fills them from — which is exactly the part that's
missing today.

## Try the demo

**Demo bot:** launching shortly — email me and I'll ping you the day it's
live. You'll text it something like `poured concrete 3rd floor section B,
12 cubic meters` + a photo and get back the structured entry.
Limited to 5 entries/day.

## What's in the full kit ($39)

- Python source (aiogram 3) — deploy on any VPS in an evening
- Claude-powered free-text mapping with a **pluggable trade vocabulary**:
  work types, units (imperial or metric), job names — tuned in one file
- Daily log export: per-job, per-day sheet (Excel) + dated photo log filed
  by job/date with an index
- SQLite record + weekly rollup by job and work type
- Deploy guide: systemd service, token setup, backup

**Early access:** the English kit is being finalized. Email
a.gorbatov80@gmail.com with subject "Site-Report Bot — early access" —
you get it first, at the launch price ($39, USDT).

Need it adapted — different language, different trade, CRM integration?
Custom work is available: a.gorbatov80@gmail.com

More kits: [automation-kits storefront](https://automation-kits.pages.dev/c/gh)

## FAQ

**Does the crew need to install anything?** No — they text a Telegram bot like
any other chat. Photos with a caption become an entry; photos without one attach
to the crew member's last entry.

**Where does the data live?** On your own VPS, in SQLite. Nothing goes to a
third-party service except the text sent to the AI API for field mapping —
and the vocabulary file lets you control exactly what's sent.

**What does running it cost?** A $5/month VPS + AI API usage (a few cents per
crew per day at typical volumes — one short text per report).

**Which trades does the vocabulary cover?** Concrete, framing, electrical,
plumbing, drywall, roofing out of the box — US (imperial) and UK (metric)
variants included. It's one Python file; adding your trade's terms takes minutes.

## Changelog

- **2026-08-02** — English kit finalized (aiogram 3, US/UK vocabulary layers,
  daily log + weekly rollup + photo index exports); early access open while the
  live demo bot is being set up.
- **2026-08-01** — teaser published; production pipeline (photo intake, SQLite
  log, summaries) running daily on a live school build with 4 crews.
