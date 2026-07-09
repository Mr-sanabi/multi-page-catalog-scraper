# Multi-page Catalog Scraper

Python CLI scraper for extracting book data from multiple catalog pages and exporting CSV, JSON, and Markdown reports.

## Features

- Scrapes multiple catalog pages
- Extracts book title, price, availability, rating, and product URL
- Handles relative product links from catalog cards
- Saves scraped data to CSV
- Saves scraped data to JSON
- Generates a Markdown summary report
- Counts books by rating
- Counts books by availability status
- Provides CLI arguments for page count and output paths
- Shows scraping progress with logging

## Tech Stack

- Python
- Requests
- BeautifulSoup
- CSV
- JSON
- argparse
- logging
- pathlib

## Project Structure

    multi-page-catalog-scraper/
      src/
        main.py
        fetcher.py
        parser.py
        writer.py
        reporter.py
        logger_config.py

      data/
        processed/
          books.csv
          books.json

      reports/
        report.md

      logs/
      README.md
      requirements.txt
      .gitignore

## Usage

Install dependencies:

    pip install -r requirements.txt

Run the scraper from the project root:

    python src/main.py --pages 3 --csv data/processed/books.csv --json data/processed/books.json --report reports/report.md

Example with 5 pages:

    python src/main.py --pages 5 --csv data/processed/books.csv --json data/processed/books.json --report reports/report.md

## CLI Arguments

    --pages    Number of catalog pages to scrape
    --csv      Path for the CSV output file
    --json     Path for the JSON output file
    --report   Path for the Markdown report

## Output

The pipeline generates:

    data/processed/books.csv
    data/processed/books.json
    reports/report.md

Each scraped book record contains:

    title
    price
    availability
    rating
    product_url

## Report Contents

The Markdown report includes:

- Number of pages scraped
- Total number of books
- Rating distribution
- Availability distribution
- Sample scraped records

Example sections:

    # Catalog Scraping Report

    ## Summary
    - Pages scraped: 3
    - Total books: 60

    ## Ratings
    - One: 15
    - Two: 8
    - Three: 13
    - Four: 10
    - Five: 14

    ## Availability
    - In stock: 60

## Target Website

This project uses Books to Scrape, a public demo website for web scraping practice:

    https://books.toscrape.com/

## Purpose

This project demonstrates a clean scraping pipeline:

    catalog page URL
    → fetch HTML
    → parse book cards
    → extract structured records
    → export CSV
    → export JSON
    → generate Markdown report

It is designed as a portfolio project for web scraping, data extraction, CLI automation, and structured output generation.

## Status

Portfolio-ready v1.