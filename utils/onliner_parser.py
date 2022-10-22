from datetime import datetime
from http import HTTPStatus

from aiohttp import ClientSession
from bs4 import BeautifulSoup as bs


async def get_response():
    async with ClientSession(base_url='https://realt.onliner.by') as session:
        response = await session.get(
            url='/'
        )
        if response.status == HTTPStatus.OK:
            return await response.text()


async def parse_html(html: str):
    data_month = {
        'декабря': '12',
        "января": '1',
        "февраля": '2',
        "марта": '3',
        "апреля": '4',
        "мая": '5',
        "июня": '6',
        "июля": '7',
        "августа": '8',
        "сентября": '9',
        "октября": '10',
        "ноября": '11',
    }
    soup = bs(html, features='html.parser')
    news_block = soup.find('div', class_='news-tidings__list')
    divs = news_block.find_all('div', class_='news-tiles__time')
    urls = news_block.find_all('a', class_='news-tiles__stub')
    date_now = datetime.now()
    news = []
    for i in range(len(divs)):
        date_published = divs[i].get_text().replace('в ', '').strip()
        for month in data_month:
            if month in date_published:
                date_published = date_published.replace(month, data_month.get(month))
                break
        date_published = datetime.strptime(date_published, '%d %m %Y %H:%M')
        delta = date_now - date_published
        if delta.total_seconds() <= 3610 * 5:
            news.append(urls[i]['href'])
    return news
