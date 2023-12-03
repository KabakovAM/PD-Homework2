from django.core.management.base import BaseCommand
from Ex008.models import Good

class Command(BaseCommand):
    help = 'Create good'
  
    def handle (self, *args, **kwargs):
        good = Good(name='Good1', description = 'Description1', price = 100, quantity  = 100)
        good.save()
        self.stdout.write(f'{good}')