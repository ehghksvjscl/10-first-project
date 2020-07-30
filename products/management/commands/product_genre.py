from django.core.management.base import BaseCommand, no_translations
from products import models
import csv


class Command(BaseCommand):
    @no_translations
    def handle(self, *args, **options):
        # db 경로 설정
        CSV_PATH_PRODUCTS = (
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/유형별/by_type_toner_mist_1.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/유형별/by_type_serum_essence_2.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/유형별/by_type_cream_lotion_3.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/유형별/by_type_mask_pack_4.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/유형별/by_type_Suncare_5.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/유형별/by_type_BB_cream_6.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/유형별/by_type_Make_up_7.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/유형별/by_type_cleansing_8.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/유형별/by_type_Scrub_Filling_9.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/유형별/by_type_body_care_10.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/유형별/by_type_lip_eye_11.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/유형별/by_type_ACC_12.csv",
        )
        index = 0
        # 파일읽기
        for PATH in CSV_PATH_PRODUCTS:
            with open(PATH) as in_file:
                data_reader = csv.reader(in_file)
                next(data_reader, None)
                index += 1
                for row in data_reader:
                    pk = models.Genre_Category.objects.get(pk=index)
                    if models.Product.objects.filter(name=row[0]).exists():  # 기존 DB에 같은 제품이 존재할 경우
                        product_pk = models.Product.objects.get(name=row[0])
                        product_pk.genre_id = pk.id
                        product_pk.save()
                        models.Distinct_Product(
                            name=row[0],
                            genre_id=pk.id,
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
                            genre_id=pk.id,
                            flag_id=plag_pk.id,
                            product_detail_id=product_detail_pk.id,
                            is_main=False
                        ).save()
