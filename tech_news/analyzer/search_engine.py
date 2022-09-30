
from ..database import search_news
from datetime import datetime


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
    try:
        listTitle = []
        d1 = datetime.strptime(date, '%Y-%m-%d')
        dataFormat = str(d1).split()[0]
        data = dataFormat.split('-')
        dataformatCorrect = f"{data[2]}/{data[1]}/{data[0]}"
        db = search_news({"timestamp": {"$regex": dataformatCorrect}})
        if(db == []):
            listTitle.append([])
            return []
        for i in db:
            tupla = (i["title"], i["url"])
            listTitle.append(tupla)
            return listTitle
    except ValueError:
        raise ValueError('Data inválida')


# print(search_by_date('2022-09-28'))


# Requisito 8
def search_by_tag(tag):
    listTag = []
    db = search_news({"tags": {"$elemMatch": {"$regex": tag, "$options": "i"}}})
    if(db == []):
        listTag.append([])
        return []
    for i in db:
        tupla = (i["title"], i["url"])
        listTag.append(tupla)
    return listTag


# print(search_by_tag('tecnologia'))


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
