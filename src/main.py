from fetcher import fetch_html
from parser import parse_books

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

    print(len(all_books))
    
    


if __name__ == "__main__":
    main()