# Multi-page Catalog Scraper

A Python CLI that collects books from Books to Scrape across several pages and saves CSV, JSON, and a Markdown report.

## Run

```bash
python -m pip install -r requirements.txt
python src/main.py --pages 3
```

Outputs: `data/processed/books.csv`, `data/processed/books.json`, and `reports/report.md`.
Fields: `title`, `price`, `availability`, `rating`, `product_url`.

Set custom paths with `--csv`, `--json`, and `--report`; run `python src/main.py --help` for options.

## Limits

Built for the Books to Scrape practice site, not arbitrary catalogs. Failed pages are logged and skipped, so output can be partial. No output is written if no records are collected.
Other sites need their own selectors and access checks.
