from django.core.management.base import BaseCommand, no_translations
from products import models
import csv


class Command(BaseCommand):
    @no_translations
    def handle(self, *args, **options):
        # db 경로 설정
        CSV_PATH_PRODUCTS = (
            "/home/spectre/바탕화면/Python/crawling/python/products_review_url.csv"
        )
        # 파일읽기
        with open(CSV_PATH_PRODUCTS) as in_file:
            data_reader = csv.reader(in_file)
            next(data_reader, None)
            for row in data_reader:
                pk = models.Product.objects.get(id=row[0])
                star_5 = int(row[6])
                star_4 = int(row[5])
                star_3 = int(row[4])
                star_2 = int(row[3])
                star_1 = int(row[2])
                try:
                    star_avg = (
                        star_1
                        + (star_2 * 2)
                        + (star_3 * 3)
                        + (star_4 * 4)
                        + (star_5 * 5)
                    ) / (star_1 + star_2 + star_3 + star_4 + star_5)
                except ZeroDivisionError:
                    star_avg = 0
                pk.star_average = star_avg
                pk.save()
