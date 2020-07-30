from django.core.management.base import BaseCommand, no_translations
from products import models
import csv


class Command(BaseCommand):
    @no_translations
    def handle(self, *args, **options):
        models.Menu(name="제품").save()
        models.Menu(name="이벤트").save()
        models.Menu(name="스토리").save()
