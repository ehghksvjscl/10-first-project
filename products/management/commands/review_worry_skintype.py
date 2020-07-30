from django.core.management.base import BaseCommand, no_translations
from reviews import models as review_models
import csv


class Command(BaseCommand):
    @no_translations
    def handle(self, *args, **options):
        review_models.SkinType(name="없음").save()
        review_models.SkinType(name="건성").save()
        review_models.SkinType(name="지성").save()
        review_models.SkinType(name="복합성").save()
        review_models.Worry(name="없음").save()
        review_models.Worry(name="칙칙함").save()
        review_models.Worry(name="건조함").save()
        review_models.Worry(name="민감성").save()
        review_models.Worry(name="트러블").save()
        review_models.Worry(name="모공").save()
        review_models.Worry(name="노화").save()
