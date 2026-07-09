from fetcher import fetch_html
from parser import parse_books
from writer import save_csv, save_json, save_text

def main():
    test_url = "https://books.toscrape.com/catalogue/page-1.html"

    
    all_books = []
    max_pages = 3

    for page_number in range(1, max_pages + 1):
        page_url = f"https://books.toscrape.com/catalogue/page-{page_number}.html"
        html = fetch_html(page_url)
        print(page_url)
        books = parse_books(html)

        all_books.extend(books)

    save_csv("data/processed/books.csv", all_books)
    save_json("data/processed/books.json", all_books)
    
    


if __name__ == "__main__":
    main()