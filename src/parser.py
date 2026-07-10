from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_text_or_empty(parent, selector):
    tag = parent.select_one(selector)
    if tag:
        return tag.get_text(strip=True)
    else:
        return ""
    
def get_attr_or_empty(parent, selector, attr):
    tag = parent.select_one(selector)
    if tag and tag.has_attr(attr):
        return tag[attr]
    else:
        return ""
    
def extract_book(card):
    title = get_attr_or_empty(card, "h3 a", "title")
    price = get_text_or_empty(card, ".price_color")
    availability = get_text_or_empty(card, ".availability")
    rating_tag = card.select_one("p.star-rating")
    product_url = get_attr_or_empty(card, "h3 a", "href")
    base_url = "https://books.toscrape.com/catalogue/"

    if rating_tag and rating_tag.has_attr("class"):
        rating = rating_tag["class"][1]
    else:
        rating = ""
    
    return {
        "title": title,
        "price": price,
        "availability": availability,
        "rating": rating,
        "product_url": urljoin(base_url, product_url)
    }
    

def parse_books(html):
    soup = BeautifulSoup(html, "html.parser")
    cards = soup.select(".product_pod")
    books = []
    for card in cards:
        books_list = extract_book(card)
        books.append(books_list)

    return books