from django.core.management.base import BaseCommand, no_translations
from reviews import models as review_models
from products import models as product_models
import csv
import re


class Command(BaseCommand):
    @no_translations
    def handle(self, *args, **options):
        # db 경로 설정
        CSV_PATH_PRODUCTS = (
            "/home/spectre/바탕화면/Python/crawling/python/products_detail_review.csv"
        )
        # 파일읽기
        with open(CSV_PATH_PRODUCTS) as in_file:
            data_reader = csv.reader(in_file)
            next(data_reader, None)
            for row in data_reader:
                pk = product_models.Product.objects.get(id=row[0])
                star_point = 0
                # star point
                if row[1] == "- 아주 좋아요":
                    star_point = 5
                elif row[1] == "- 맘에 들어요":
                    star_point = 4
                elif row[1] == "- 보통이에요":
                    star_point = 3
                elif row[1] == "- 그냥 그래요":
                    star_point = 2
                elif row[1] == "- 별로에요":
                    star_point = 1
                else:
                    star_point = 0

                if row[2] == "":
                    worry = 1
                else:
                    try:
                        worry = review_models.Worry.objects.get(name=row[2]).id
                    except Exception:
                        worry = 1

                if row[3] == "":
                    skintype = 1
                else:
                    skintype = review_models.SkinType.objects.get(name=row[3]).id

                content = re.sub(pattern="[^\w\s]", repl="", string=row[4])
                review_models.Review(
                    product=pk,
                    star_point=star_point,
                    worry_id=worry,
                    skintype_id=skintype,
                    content=content,
                    image_url=row[5],
                ).save()
