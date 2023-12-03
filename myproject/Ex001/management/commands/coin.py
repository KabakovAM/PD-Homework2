from django.core.management.base import BaseCommand
from Ex001.models import Coin
from random import choice

class Command(BaseCommand):
    help = 'Create coin'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Coin count')
    
    def handle (self, *args, **kwargs):
        count = kwargs.get('count')
        for _ in range(count):
            coin = Coin(coin=choice(['Орёл', 'Решка']))
            coin.save()


