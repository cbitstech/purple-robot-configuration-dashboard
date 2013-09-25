from django.core.management.base import BaseCommand, CommandError
from templates.models import Template
import json

class Command(BaseCommand):
    args = '<json object>'
    help = 'Loads the configuration schema'

    def handle(self, *args, **options):
        template = open('/static/template.json')
        
