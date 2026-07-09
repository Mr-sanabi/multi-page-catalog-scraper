import argparse
import logging
from fetcher import fetch_html
from parser import parse_books
from writer import save_csv, save_json, save_text
from reporter import build_report
from logger_config import setup_logging

def parse_args():

    parser = argparse.ArgumentParser(
        description="description"
    )
    parser.add_argument("--pages", type=int)
    parser.add_argument("--csv")
    parser.add_argument("--json")
    parser.add_argument("--report")
    return parser.parse_args()


def main():
    args = parse_args()
    setup_logging()

    all_books = []

    for page_number in range(1, args.pages + 1):
        logging.info(f"Scraping page: {page_number}...")
        page_url = f"https://books.toscrape.com/catalogue/page-{page_number}.html"
        html = fetch_html(page_url)
        books = parse_books(html)

        all_books.extend(books)

    logging.info(f"Parsed {len(all_books)} books")

    logging.info("Saving CSV...")
    save_csv(args.csv, all_books)

    logging.info("Saving JSON...")
    save_json(args.json, all_books)

    logging.info("Generating report...")
    report = build_report(all_books, args.pages)
    save_text(args.report, report)

    logging.info("Pipeline completed")


if __name__ == "__main__":
    main()