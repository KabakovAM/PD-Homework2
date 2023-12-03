from django.core.management.base import BaseCommand
from Ex001.models import Coin

class Command(BaseCommand):
    help = 'Coin Stat'

    def add_arguments(self, parser):
        parser.add_argument('last count', type=int, help='last count')
    
    def handle (self, *args, **kwargs):
        last_count = kwargs.get('last count')
        coins = Coin.objects.order_by('-pk')[:last_count]
        self.stdout.write(f'{coins}')

