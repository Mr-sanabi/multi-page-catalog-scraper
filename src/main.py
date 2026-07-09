from fetcher import fetch_html

def main():
    test_url = "https://books.toscrape.com/catalogue/page-1.html"
    html = fetch_html(test_url)
    print(html[:500])


if __name__ == "__main__":
    main()