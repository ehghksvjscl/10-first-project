from django.core.management.base import BaseCommand, no_translations
from products import models
import csv


class Command(BaseCommand):
    @no_translations
    def handle(self, *args, **options):
        # db 경로 설정
        CSV_PATH_PRODUCTS = ("/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/온라인세트/by_line_online_set_1.csv",)
        # 파일읽기
        for PATH in CSV_PATH_PRODUCTS:
            index = 0
            with open(PATH) as in_file:
                data_reader = csv.reader(in_file)
                next(data_reader, None)
                index += 1
                for row in data_reader:
                    pk = models.Online_Category.objects.get(pk=index)
                    if models.Product.objects.filter(name=row[0]):  # 기존 DB에 같은 제품이 존재할 경우
                        product_pk = models.Product.objects.get(name=row[0])
                        product_pk.online_id = pk.id
                        product_pk.save()
                        models.Distinct_Product(
                            name=row[0],
                            online_id=pk.id,
                        ).save()
                    else:  # 기존 DB에 없는 경우
                        plag_pk = models.Product_Plag.create(
                            flag_new = row[6],
                            flag_gift = row[4],
                            flag_sale = row[3],
                            flag_best = row[5],
                        )
                        product_detail_pk = models.Product_Detail.create(
                            tag=row[1],
                            price=row[8].replace(",", ""),
                            price_sale=row[9].replace(",", ""),
                        )
                        models.Product(
                            name=row[0],
                            main_image_url=row[2],
                            online_id=pk.id,
                            flag_id=plag_pk.id,
                            product_detail_id=product_detail_pk.id,
                            is_main=False
                        ).save()