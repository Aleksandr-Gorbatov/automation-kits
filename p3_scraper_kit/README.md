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

**Get the full kit:** https://nowpayments.io/payment/?iid=4330910215 (USDT).
Delivery by email within 24 hours of payment (usually much sooner) — I check payments
personally, not a bot. Nothing after 24h? Email me the payment ID: immediate delivery
or a full refund.

Questions or a custom scraping task? → a.gorbatov80@gmail.com

## Rules of the road

Scrape politely: respect `robots.txt`, keep request rates human-scale, put a
real contact in your User-Agent. This kit deliberately ships **no** tooling for
bypassing anti-bot protections — nobody can promise "100% stability against
anti-bot" anyway, and the vendors who do are selling you a ban.

MIT license — free tier (`scraper_kit.py`) only. The paid examples and snapshot-delta
module are licensed for your own projects (any number), not for redistribution or resale.
Built by an engineer who runs these daily.
