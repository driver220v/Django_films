from django.core.management.base import BaseCommand

from scrapper.management.scrape_utils.scrapper_gather import main_gather
from scrapper.management.scrape_utils.scrapper_parse import main_parse
from scrapper.models import Film


class Command(BaseCommand):
    help = 'Start scrape-parse Function'

    def handle(self):
        main_parse(main_gather())
        Film.objects.all()
        print('ok')
        return 'ok'
