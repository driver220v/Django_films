import requests
from bs4 import BeautifulSoup

from .models import Film
from scrapper_gather import main_gather as get_links


# Парсинг и попытка сохранить в БД
def get_url_content(url):
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'lxml')
        title_raw_header_below = soup.find('h1', class_='mop-ratings-wrap__title mop-ratings-wrap__title--top')
        title_raw_under_header = soup.find('span', class_='mop-ratings-wrap__title--small')

        tomatores = soup.find('div', class_='mop-ratings-wrap__half critic-score')
        auidience = soup.find('div', class_='mop-ratings-wrap__half audience-score')

        title = None
        tomatores_score = None
        auidience_score = None
        premier = None
        genre_type = None
        if len(title_raw_under_header.text) == 0:
            title = title_raw_header_below.text.strip()
        else:
            title = title_raw_under_header.text.strip()

        try:
            genre_raw = soup.find(text="Genre:")
            genre_type = genre_raw.find_next().text.strip()
        except AttributeError:
            genre_type = 'Null'

        try:
            premier_raw = soup.find(text="Premiere Date:")
            premier = premier_raw.find_next().text.strip()
        except AttributeError:
            premier = 'Null'

        try:
            tomatores_score = tomatores.find('span', class_='mop-ratings-wrap__percentage').text.strip()
        except AttributeError:
            tomatores_score = 'Null'
        try:
            auidience_score = auidience.find('span', class_='mop-ratings-wrap__percentage').text.strip()
        except AttributeError:
            auidience_score = 'Null'

        # Какие поля нужно заполнить в БД
        # film_id = models.IntegerField(null=False, unique=True, serialize=True)
        # title = models.CharField(max_length=50, null=False)
        # genre = models.CharField(max_length=40)
        # premier = models.DateTimeField(max_length=4)  # todo выставить правильный формат
        # avg_tomatometer = models.CharField(max_length=3)  # todo Percentage
        # avg_audience_score = models.CharField(max_length=3)  # todo Percentage
        if len(title) != 0 and len(tomatores_score) != 0 and len(auidience_score) != 0 and len(genre_type) != 0 and len(
                premier) != 0:

            print(title, tomatores_score, auidience_score, genre_type, premier)
            f = Film(title=title, avg_tomatometer=tomatores_score, avg_audience_score=auidience_score, genre=genre_type,
                     premier=premier)
            f.save()


def main_parse(lst_links):
    for url in lst_links:
        get_url_content(url)


main_parse(get_links())
