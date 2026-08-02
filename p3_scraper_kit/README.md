# Resumable Scraper Kit — free tier

Scrapers die: a 429, a dropped connection, a layout change, a Ctrl+C.
The difference between a toy and a tool is what happens **next**.

This kit is the skeleton I use in monitors that run in production every day.
The free tier gives you the two pieces that stop you from ever re-scraping
from zero:

- **`Checkpoint`** — progress is persisted every N items (atomic writes).
  Crash at item 3 741 → next run resumes at 3 742.
- **`fetch()`** — exponential backoff with jitter on 429/5xx and network
  errors, honours `Retry-After`, sets an honest User-Agent.

What it looks like in practice:

```text
$ python my_scraper.py
got page 3739  [checkpoint saved]
got page 3740  [checkpoint saved]
^C  — killed mid-run
$ python my_scraper.py
resuming: 3 741 done, continuing at 3 742
...
$ python my_scraper.py     # next morning
second run: 0 new items — delta working
```

## Quick start

```bash
pip install requests
python scraper_kit.py     # toy demo: kill it mid-run, start again — it resumes
```

Use it in your own scraper:

```python
from scraper_kit import Checkpoint, fetch

urls = load_urls_somehow()
with Checkpoint("myjob") as cp:
    for url in cp.remaining(urls):
        html = fetch(url).text
        parse_and_save(html)
        cp.done(url)
```

## What the full kit adds ($19)

| Free tier | Full kit |
|---|---|
| Checkpoints + retries | everything on the left, plus: |
| | **Snapshot-delta** — repeat runs return only *new* items (the `seen.json` pattern) |
| | **Worked example 1**: scraping JSON-LD listings (jobs, products, events) |
| | **Worked example 2**: scraping HTML cards with CSS selectors |
| | **Adaptation guide** — point the kit at your site in ~1 hour |

**Get the full kit:** https://nowpayments.io/payment/?iid=4330910215 (USDT) ·
[all kits & how buying works](https://automation-kits.pages.dev/c/gh).
Delivery by email within 24 hours of payment (usually much sooner) — I check payments
personally, not a bot. Nothing after 24h? Email me the payment ID: immediate delivery
or a full refund.

Questions or a custom scraping task? → a.gorbatov80@gmail.com

## FAQ

**Why USDT and not a card?** Card checkout isn't available to me yet — the invoice
page walks you through paying from any wallet or exchange. You always have my email
and a receipt; the refund policy above applies either way.

**Does it work with Selenium / Playwright?** The `Checkpoint` class is
transport-agnostic — wrap any fetch loop with it. The built-in `fetch()` is
`requests`-based; browser automation is out of scope on purpose (heavier, and
most listing-type sites don't need it).

**Python version?** 3.9+. Only dependency is `requests`.

**Can I use it in client projects?** Yes — the full kit is licensed for any number
of your own or client projects; redistribution/resale of the kit itself is not allowed.

## Changelog

- **2026-08-01** — v1.0: first public release (checkpoints + retry engine in the
  free tier; snapshot-delta and two worked examples in the full kit).
- **2026-08-02** — README: added terminal demo, FAQ, this changelog.

## Rules of the road

Scrape politely: respect `robots.txt`, keep request rates human-scale, put a
real contact in your User-Agent. This kit deliberately ships **no** tooling for
bypassing anti-bot protections — nobody can promise "100% stability against
anti-bot" anyway, and the vendors who do are selling you a ban.

MIT license — free tier (`scraper_kit.py`) only. The paid examples and snapshot-delta
module are licensed for your own projects (any number), not for redistribution or resale.
Built by an engineer who runs these daily.
