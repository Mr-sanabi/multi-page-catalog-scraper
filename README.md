# Multi-page Catalog Scraper

A Python CLI tool that extracts book data from multiple catalog pages and exports structured CSV, JSON, and Markdown outputs.

The project uses [Books to Scrape](https://books.toscrape.com/), a public website created for web scraping practice.

## Features

- Scrapes a configurable number of catalog pages
- Extracts title, price, availability, rating, and product URL
- Converts relative product links into absolute URLs
- Exports records to CSV and JSON
- Generates a Markdown summary report
- Counts books by rating and availability
- Validates that the requested page count is greater than zero
- Provides default output paths with optional CLI overrides
- Uses a request timeout to prevent stalled connections
- Handles HTTP and network errors without crashing the pipeline
- Logs failed or empty pages and continues processing
- Reports the number of successfully scraped pages
- Creates missing parent directories for output files automatically
- Shows pipeline progress through terminal and file logging

## Tech Stack

- Python
- Requests
- Beautiful Soup
- `argparse`
- `logging`
- `pathlib`
- CSV and JSON standard-library modules

## Project Structure

```text
multi-page-catalog-scraper/
├── src/
│   ├── main.py
│   ├── fetcher.py
│   ├── parser.py
│   ├── writer.py
│   ├── reporter.py
│   └── logger_config.py
├── data/
│   └── processed/
│       ├── books.csv
│       └── books.json
├── reports/
│   └── report.md
├── logs/
├── README.md
├── requirements.txt
└── .gitignore
```

## Installation

Clone the repository and enter the project directory:

```bash
git clone https://github.com/Mr-sanabi/multi-page-catalog-scraper.git
cd multi-page-catalog-scraper
```

Create and activate a virtual environment, then install the dependencies:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

macOS or Linux:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

Scrape three pages and use the default output paths:

```bash
python src/main.py --pages 3
```

Use custom output paths:

```bash
python src/main.py --pages 3 --csv custom/data/books.csv --json custom/data/books.json --report custom/reports/report.md
```

Missing output directories are created automatically.

## CLI Arguments

| Argument | Required | Default | Description |
| --- | --- | --- | --- |
| `--pages` | Yes | — | Number of catalog pages to scrape. Must be greater than zero. |
| `--csv` | No | `data/processed/books.csv` | Destination path for the CSV output. |
| `--json` | No | `data/processed/books.json` | Destination path for the JSON output. |
| `--report` | No | `reports/report.md` | Destination path for the Markdown report. |

Display the built-in help:

```bash
python src/main.py --help
```

## Output Schema

Each book record contains:

| Field | Description |
| --- | --- |
| `title` | Book title |
| `price` | Displayed catalog price |
| `availability` | Availability text from the catalog |
| `rating` | Text rating from `One` to `Five`; empty when unavailable |
| `product_url` | Absolute URL of the product page |

Example JSON record:

```json
{
  "title": "A Light in the Attic",
  "price": "£51.77",
  "availability": "In stock",
  "rating": "Three",
  "product_url": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
}
```

## Generated Files

With the default settings, the pipeline creates:

```text
data/processed/books.csv
data/processed/books.json
reports/report.md
logs/log.txt
```

The Markdown report includes:

- successfully scraped page count
- total book count
- rating distribution
- availability distribution
- five sample records

Example summary for three successful pages:

```text
## Summary
- Pages scraped: 3
- Total books: 60
```

## Reliability

Each HTTP request uses a timeout and status validation. Network failures, unsuccessful HTTP responses, and empty pages are logged without terminating the entire run. Failed pages are excluded from the successful-page count.

If no books are collected, the pipeline logs an error and stops before writing empty output files.

## Pipeline

```text
catalog page URLs
→ fetch HTML
→ parse book cards
→ normalize records and product URLs
→ export CSV and JSON
→ generate Markdown report
```

## Purpose

This project demonstrates a modular scraping pipeline with multi-page extraction, structured outputs, CLI configuration, logging, validation, and basic failure handling. It is intended as a portfolio example for web scraping, data extraction, and Python automation.

## Status

Portfolio-ready v1.1
