import argparse
from fetcher import fetch_html
from parser import parse_books
from writer import save_csv, save_json, save_text
from reporter import build_report

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
    
    all_books = []

    for page_number in range(1, args.pages + 1):
        page_url = f"https://books.toscrape.com/catalogue/page-{page_number}.html"
        html = fetch_html(page_url)
        print(page_url)
        books = parse_books(html)

        all_books.extend(books)

    save_csv(args.csv, all_books)
    save_json(args.json, all_books)
    report = build_report(all_books, args.pages)
    save_text(args.report, report)
    


if __name__ == "__main__":
    main()