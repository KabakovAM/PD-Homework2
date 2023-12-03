from django.core.management.base import BaseCommand
from Ex008.models import Client

class Command(BaseCommand):
    help = 'Create client'
  
    def handle (self, *args, **kwargs):
        client = Client(name='Client1', email = 'email1@example.com', phone = 'phone1', adress = 'adress1')
        client.save()
        self.stdout.write(f'{client}')