from django.core.management.base import BaseCommand, no_translations
from products import models
import csv

class Command(BaseCommand):
    @no_translations
    def handle(self, *args, **options):
        # db 경로 설정
        CSV_PATH_PRODUCTS = (
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/라인별/by_line_biom_1.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/라인별/by_line_Solavaiom_2.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/라인별/by_line_Cicapair_3.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/라인별/by_line_ControlA_4.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/라인별/by_line_seramydine_5.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/라인별/by_line_cryo_rubber_6.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/라인별/by_line_evry_sun_day_7.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/라인별/by_line_V7_8.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/라인별/by_line_the_mask_9.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/라인별/by_line_dermaclair_10.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/라인별/by_line_The_Makeup_11.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/라인별/by_line_RX_12.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/라인별/by_line_peptidine_13.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/라인별/by_line_Foreman_14.csv",
            "/home/spectre/바탕화면/wecode/10-DrMozart-backend/db/라인별/by_line_non-peptide_15.csv"
        )
        index = 0
        # 파일읽기
        for PATH in CSV_PATH_PRODUCTS:
            with open(PATH) as in_file:
                data_reader = csv.reader(in_file)
                next(data_reader, None)
                index += 1
                print(PATH)
                for row in data_reader:
                    pk = models.Line_Category.objects.get(pk=index)
                    if models.Product.objects.filter(name=row[0]).exists():  # 기존 DB에 같은 제품이 존재할 경우
                        product_pk = models.Product.objects.get(name=row[0])
                        product_pk.line = pk
                        product_pk.save()
                        models.Distinct_Product(
                            name=row[0],
                            line_id=pk.id,
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
                            line=pk.id,
                            flag_id=plag_pk.id,
                            product_detail_id=product_detail_pk.id,
                            is_main=False
                        ).save()