from django.core.management.base import BaseCommand, no_translations
from products import models
import csv


class Command(BaseCommand):
    @no_translations
    def handle(self, *args, **options):
        menu_id = models.Menu.objects.get(pk=1)
        models.Skin_Category(menu=menu_id, name="회복진정").save()
        models.Skin_Category(menu=menu_id, name="수분공급").save()
        models.Skin_Category(menu=menu_id, name="트러블 케어").save()
        models.Skin_Category(menu=menu_id, name="SUN 케어").save()
        models.Skin_Category(menu=menu_id, name="안티폴루션").save()
        models.Skin_Category(menu=menu_id, name="보습장벽케어").save()
        models.Skin_Category(menu=menu_id, name="커버케어").save()
        models.Skin_Category(menu=menu_id, name="미백광채").save()
        models.Skin_Category(menu=menu_id, name="결/각질케어").save()
        models.Skin_Category(menu=menu_id, name="안티에이징").save()
        models.Skin_Category(menu=menu_id, name="스팟관리").save()
        models.Skin_Category(menu=menu_id, name="모방관리").save()

        models.Genre_Category(menu=menu_id, name="토너/미스트").save()
        models.Genre_Category(menu=menu_id, name="세럼/에센스").save()
        models.Genre_Category(menu=menu_id, name="크림/로션").save()
        models.Genre_Category(menu=menu_id, name="마스크/팩").save()
        models.Genre_Category(menu=menu_id, name="선케어").save()
        models.Genre_Category(menu=menu_id, name="비비크림").save()
        models.Genre_Category(menu=menu_id, name="메이크업").save()
        models.Genre_Category(menu=menu_id, name="클렌징").save()
        models.Genre_Category(menu=menu_id, name="스크럽/필링").save()
        models.Genre_Category(menu=menu_id, name="바디케어").save()
        models.Genre_Category(menu=menu_id, name="립/아이").save()
        models.Genre_Category(menu=menu_id, name="ACC").save()

        models.Line_Category(menu=menu_id, name="바이옴").save()
        models.Line_Category(menu=menu_id, name="솔라바이옴").save()
        models.Line_Category(menu=menu_id, name="시카페어").save()
        models.Line_Category(menu=menu_id, name="컨트롤에이").save()
        models.Line_Category(menu=menu_id, name="세라마이딘").save()
        models.Line_Category(menu=menu_id, name="크라이오 러버").save()
        models.Line_Category(menu=menu_id, name="에브리 선 데이").save()
        models.Line_Category(menu=menu_id, name="V7").save()
        models.Line_Category(menu=menu_id, name="더마스크").save()
        models.Line_Category(menu=menu_id, name="더마클리어").save()
        models.Line_Category(menu=menu_id, name="더메이크업").save()
        models.Line_Category(menu=menu_id, name="알엑스").save()
        models.Line_Category(menu=menu_id, name="펩타이딘").save()
        models.Line_Category(menu=menu_id, name="포맨").save()
        models.Line_Category(menu=menu_id, name="비 펩타이드").save()

        models.Online_Category(menu=menu_id, name="main").save()
