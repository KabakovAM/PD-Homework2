from django.core.management.base import BaseCommand
from Ex008.models import Order, Client, Good

class Command(BaseCommand):
    help = 'Create Order'
  
    def handle (self, *args, **kwargs):
        order = Order(client = Client.objects.get(pk=1))
        order.save()
        order.good.add(1)
        order.total = 100
        order.save()
        self.stdout.write(f'{order}')

