from django.core.management.base import BaseCommand, no_translations
from products import models
import csv


class Command(BaseCommand):
    @no_translations
    def handle(self, *args, **options):
        # db 경로 설정
        CSV_PATH_PRODUCTS = (
            "/home/spectre/바탕화면/Python/crawling/python/products_detail.csv"
        )
        # 파일읽기
        with open(CSV_PATH_PRODUCTS) as in_file:
            data_reader = csv.reader(in_file)
            next(data_reader, None)
            for row in data_reader:
                pk_product_detail = models.Product_Detail.objects.filter(id=row[0])
                pk_product_detail.update(detail_html=row[5]) 

                pk = models.Product_Detail.objects.get(id=row[0])
                
                if row[1] != "":
                    pk_image = models.Image.objects.create(image_url=row[1])
                    models.Product_Detail_Image.objects.create(image=pk_image,product_detail=pk)
                if row[2] != "":
                    pk_image = models.Image.objects.create(image_url=row[2])
                    models.Product_Detail_Image.objects.create(image=pk_image,product_detail=pk)
                if row[3] != "":
                    pk_image = models.Image.objects.create(image_url=row[3])
                    models.Product_Detail_Image.objects.create(image=pk_image,product_detail=pk)
                if row[4] != "":
                    pk_image = models.Image.objects.create(image_url=row[4])
                    models.Product_Detail_Image.objects.create(image=pk_image,product_detail=pk)                    


