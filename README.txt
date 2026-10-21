TENDER RADAR - PRODUCTION FILES
================================

An EV-charging tender tracker. A scheduled job scrapes government tender
portals, keeps the EV-charging tenders, saves them to a JSON file, and a
static dashboard (GitHub Pages) displays them. Optionally emails a digest.


WHAT IS IN HERE
---------------

scraper.py                  Entry point. Run: python scraper.py
sources.json                List of tender portals to check (enable/disable here)
requirements.txt            Python dependencies (requests, beautifulsoup4, playwright)
email_template.html         HTML body of the email digest
email_template.txt          Plain-text body of the email digest
.gitignore                  Ignores caches

tender_radar/               The scraper package
    pipeline.py             Runs the whole scrape -> filter -> save flow
    fetchers.py             One fetcher per portal type
    browser.py              Headless browser (Playwright) setup
    parsers/                HTML parsers for each portal layout
    matching.py             Keyword matching against categories
    normalize.py, dedupe.py, store.py, models.py, config.py, sources.py
    notify.py               Email digest over SMTP

config/categories.json      Keywords that decide which tenders are kept

docs/                       The dashboard (served by GitHub Pages)
    index.html
    css/app.css
    js/                     alerts, cards, data, main, render, util
    data/tenders.json       Tender data the dashboard reads (written by the scraper)

.github/workflows/update-tenders.yml
                            Runs the scraper every 3 hours and commits the
                            updated docs/data/tenders.json back to the repo

NOTES
-----
- The workflow creates digest_state.json itself the first time an email is
  sent; it is not included here.
- To add or change tracked keywords, edit config/categories.json.
- To add or switch off a portal, edit sources.json ("enabled": true/false).
