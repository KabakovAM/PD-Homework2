from django.core.management.base import BaseCommand
from Ex008.models import Client

class Command(BaseCommand):
    help = 'Delete client by ID'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle (self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).filter()
        if client is not None:
            client.delete()
        self.stdout.write(f'{client}')