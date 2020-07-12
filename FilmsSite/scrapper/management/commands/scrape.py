from django.core.management.base import BaseCommand
from models import Film
from scrapper_gather import main_gather
from scrapper_parse import main_parse


class Command(BaseCommand):
    help = 'Start scrape-parse Function'

    def handle(self):
        main_parse(main_gather())
        Film.objects.all()
        return 'ok'
