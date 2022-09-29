from ..database import search_news


def search_by_title(title):
    listTitle = []
    db = search_news({"title": {"$regex": title, "$options": "i"}})
    if(db == []):
        listTitle.append([])
        return []
    for i in db:
        tupla = (i["title"], i["url"])
        listTitle.append(tupla)
    return listTitle


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
