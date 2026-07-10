import requests
import logging

def fetch_html(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        response.encoding = "utf-8"
        return response.text
    
    except requests.exceptions.RequestException as error:
        logging.error(f"Request error on {url}: {error}")
        return ""
    
    