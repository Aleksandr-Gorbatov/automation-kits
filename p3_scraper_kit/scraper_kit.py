# -*- coding: utf-8 -*-
"""
Resumable Scraper Kit — free tier.

A minimal skeleton for scrapers that survive restarts:
  * checkpoints  — crash or stop at item 3 741, resume at 3 742, not at zero
  * retries      — exponential backoff on 429 / 5xx / network errors
  * polite UA    — identify yourself, rotate if you must, respect robots.txt

Free tier ships checkpoints + retries.
The full kit ($19) adds: snapshot-delta (repeat runs return only NEW items),
two worked examples (JSON-LD listings and HTML cards) and a 1-hour
adaptation guide. See the link in README.

Python 3.9+, single dependency: requests.
"""

from __future__ import annotations

import json
import random
import time
from pathlib import Path

import requests

# ---------------------------------------------------------------- checkpoints

class Checkpoint:
    """Persist progress after every N items so a crash never costs the run.

    >>> cp = Checkpoint("myjob")
    >>> for url in cp.remaining(urls):
    ...     process(url)
    ...     cp.done(url)
    """

    def __init__(self, job_name: str, every: int = 20,
                 state_dir: str | Path = ".scraper_state"):
        self.path = Path(state_dir) / f"{job_name}.json"
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.every = every
        self._done: set[str] = set()
        self._unsaved = 0
        if self.path.exists():
            self._done = set(json.loads(self.path.read_text("utf-8")))

    def remaining(self, items):
        """Yield only items not yet marked done (order preserved)."""
        for item in items:
            if str(item) not in self._done:
                yield item

    def done(self, item) -> None:
        self._done.add(str(item))
        self._unsaved += 1
        if self._unsaved >= self.every:
            self.flush()

    def flush(self) -> None:
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(sorted(self._done)), "utf-8")
        tmp.replace(self.path)          # atomic: never a half-written state
        self._unsaved = 0

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.flush()


# -------------------------------------------------------------------- retries

RETRIABLE_STATUS = {429, 500, 502, 503, 504}


def fetch(url: str, *, session: requests.Session | None = None,
          tries: int = 5, base_delay: float = 2.0, timeout: float = 30.0,
          headers: dict | None = None) -> requests.Response:
    """GET with exponential backoff + jitter. Raises after `tries` failures.

    Honours Retry-After on 429 when the server sends one.
    """
    s = session or requests.Session()
    hdrs = {"User-Agent": "scraper-kit/1.0 (+contact: put-your-email-here)"}
    if headers:
        hdrs.update(headers)

    last_err: Exception | None = None
    for attempt in range(tries):
        try:
            resp = s.get(url, headers=hdrs, timeout=timeout)
            if resp.status_code not in RETRIABLE_STATUS:
                resp.raise_for_status()
                return resp
            # retriable HTTP status
            retry_after = resp.headers.get("Retry-After")
            delay = float(retry_after) if retry_after else \
                base_delay * (2 ** attempt) + random.uniform(0, 1)
            last_err = requests.HTTPError(f"{resp.status_code} for {url}")
        except (requests.ConnectionError, requests.Timeout) as e:
            delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
            last_err = e
        time.sleep(delay)
    raise RuntimeError(f"gave up on {url} after {tries} tries") from last_err


# ------------------------------------------------------------------- example

if __name__ == "__main__":
    # Toy demo: fetch a few pages with resume support.
    # Stop it with Ctrl+C mid-run, start again — it continues, not restarts.
    urls = [f"https://httpbin.org/delay/1?page={i}" for i in range(10)]

    with Checkpoint("demo", every=2) as cp:
        for url in cp.remaining(urls):
            resp = fetch(url)
            print("got", url, resp.status_code)
            cp.done(url)
    print("run complete — delete .scraper_state/demo.json to start fresh")
