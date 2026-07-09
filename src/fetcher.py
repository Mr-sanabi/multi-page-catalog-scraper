import requests

def fetch_html(url):
    response = requests.get(url)
    if response.status_code != 200:
        return ""
    else:
        response.encoding = "utf-8"
        return response.text