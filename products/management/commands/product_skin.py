from django.core.management.base import BaseCommand, no_translations
from products import models
import csv


class Command(BaseCommand):
    @no_translations
    def handle(self, *args, **options):
        # db 경로 설정
        CSV_PATH_PRODUCTS = (
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/민감/skin solution_1.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/민감/skin_moisture supply_2.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/민감/skin_Trouble_Care_3.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/민감/skin_SUN_Care_4.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/민감/skin_Antifolutions_5.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/민감/skin_Moisturizing_barrier_care_6.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/민감/skin_cover_care_7.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/민감/skin_whitening_&_glare_8.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/민감/skin solution_9.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/민감/skin_Anti-aging_10.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/민감/skin_Spot_management_11.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/민감/skin_pore_management_12.csv",
        )
        index = 0

        # 파일읽기
        for PATH in CSV_PATH_PRODUCTS:
            with open(PATH) as in_file:
                data_reader = csv.reader(in_file)
                next(data_reader, None)
                index += 1
                for row in data_reader:
                    pk = models.Skin_Category.objects.get(pk=index)
                    # print(dir(models.Product.objects.filter(name=row[0])))
                    if models.Product.objects.filter(name=row[0]).exists():  # 기존 DB에 같은 제품이 존재할 경우
                        models.Distinct_Product(
                            name=row[0],
                            skin_id=pk.id,
                        ).save()
                    else:  # 기존 DB에 없는 경우
                        plag_pk = models.Product_Plag.objects.create(
                            flag_new = row[6],
                            flag_gift = row[4],
                            flag_sale = row[3],
                            flag_best = row[5],
                        )
                        product_detail_pk = models.Product_Detail.objects.create(
                            tag=row[1],
                            price=row[8].replace(",", ""),
                            price_sale=row[9].replace(",", ""),
                        )
                        models.Product(
                            name=row[0],
                            main_image_url=row[2],
                            skin_id=pk.id,
                            flag_id=plag_pk.id,
                            product_detail_id=product_detail_pk.id,
                            is_main=False
                        ).save()
