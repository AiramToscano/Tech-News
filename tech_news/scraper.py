from parsel import Selector
import time
import requests

# Requisito 1


def fetch(url):
    try:
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        time.sleep(1)
        if response.status_code == 200:
            return response.text
    except requests.ReadTimeout:
        return None
    except requests.HTTPError:
        return None


# print(fetch("https://blog.betrybe.com/"))
# Requisito 2


def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    urlNotices = selector.css(".cs-overlay-link::attr(href)").getall()
    return urlNotices
    """Seu código deve vir aqui"""


# scrape_novidades(fetch("https://blog.betrybe.com"))
# Requisito 3


def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    nextpage = selector.css(".next.page-numbers::attr(href)").get()
    return nextpage
    """Seu código deve vir aqui"""


# scrape_next_page_link(fetch("https://blog.betrybe.com"))
# Requisito 4


def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
