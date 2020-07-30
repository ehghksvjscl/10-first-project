from django.core.management.base import BaseCommand, no_translations
from products import models
import csv


class Command(BaseCommand):
    @no_translations
    def handle(self, *args, **options):
        # db 경로 설정
        CSV_PATH_PRODUCTS = (
            "/home/spectre/바탕화면/Python/crawling/python/dr_product_main.csv"
        )
        # 파일읽기
        with open(CSV_PATH_PRODUCTS) as in_file:
            data_reader = csv.reader(in_file)
            next(data_reader, None)
            for row in data_reader:
                pk = models.Product.objects.get(name=row[0])
                pk.is_main = True
                pk.save()
