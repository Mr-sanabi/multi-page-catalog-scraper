from fetcher import fetch_html
from parser import parse_books

def main():
    test_url = "https://books.toscrape.com/catalogue/page-1.html"
    html = fetch_html(test_url)
    books = parse_books(html)
    print(len(books))
    print(books[:3])


if __name__ == "__main__":
    main()