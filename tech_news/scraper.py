from parsel import Selector
import time
import requests
from .database import create_news

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
    try:
        selector = Selector(text=html_content)
        url = selector.css("[rel=canonical]::attr(href)").get()
        title = selector.css(".entry-title::text").get()
        data = selector.css(".meta-date::text").get()
        # dataFormat = data.split()
        writer = selector.css(".url.fn.n::text").get()
        comments = selector.css(
            ".post-comments.post-comments-simple h5::text"
        ).get()
        commentsFormat = comments.split()
        summary = selector.xpath("string(//p)").get().strip()
        tags = selector.css(".post-tags a::text").getall()
        label = selector.css(".label::text").get()
        obj = {
            "url": url,
            "title": title,
            "writer": writer,
            "summary": summary,
            "comments_count": int(commentsFormat[0]),
            "timestamp": data,
            "tags": tags,
            "category": label,
        }
        return obj
    except AttributeError:
        selector = Selector(text=html_content)
        url = selector.css("[rel=canonical]::attr(href)").get()
        title = selector.css(".entry-title::text").get().strip()
        data = selector.css(".meta-date::text").get()
        # dataFormat = data.split()
        writer = selector.css(".url.fn.n::text").get()
        summary = selector.xpath("string(//p)").get().strip()
        tags = selector.css(".post-tags a::text").getall()
        label = selector.css(".label::text").get()
        obj = {
            "url": url,
            "title": title,
            "writer": writer,
            "summary": summary,
            "comments_count": 0,
            "timestamp": data,
            "tags": tags,
            "category": label,
        }
        return obj


# print(scrape_noticia(
#     fetch(
#         "https://blog.betrybe.com/carreira/livros-sobre-lideranca/"
#     )
# ))
# Requisito 5


def get_tech_news(amount):
    newamount = amount - 1
    allnotices = []
    noticesArray = []
    URL_BASE = "https://blog.betrybe.com"
    proxpage = URL_BASE
    while proxpage and allnotices.__len__() <= newamount:
        fetchapi = fetch(proxpage)
        arrayNotices = scrape_novidades(fetchapi)
        allnotices.extend(arrayNotices)
        proxpage = scrape_next_page_link(fetchapi)

    for index, link in enumerate(allnotices):
        if(index <= newamount):
            api = fetch(link)
            notices = scrape_noticia(api)
            noticesArray.append(notices)
    create_news(noticesArray)
    return noticesArray
