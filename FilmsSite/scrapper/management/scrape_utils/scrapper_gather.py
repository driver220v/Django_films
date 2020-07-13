# здесь будет происходит поиск href' и добавление в список

from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from FilmsSite.settings import SCRAPPING_URL


def rubbish_remover(url):
    scheme, netloc, path, params, query, fragment = urlparse(url)
    link_lst = [netloc, path]
    link = 'https://' + ''.join(link_lst)
    return link


def gather_hrefs(source):
    list_links = []
    soup = BeautifulSoup(source.content, 'lxml')
    page_list_films = soup.find_all('a', class_='article_movie_poster')
    for film_entries in page_list_films:
        film_link = film_entries.get('href')
        link = rubbish_remover(film_link)
        list_links.append(link)
    return list_links


def request_initial_page(url_init):
    page = requests.get(url_init)
    page_code = page.status_code
    if page_code == 200:
        links_list = gather_hrefs(page)
        return links_list


def main_gather():

    links_list = request_initial_page(SCRAPPING_URL)
    return links_list
