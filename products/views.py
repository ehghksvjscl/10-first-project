import random

from django.views import View
from django.http import JsonResponse

from . import models
from reviews import models as reviews_models


class MainView(View):
    def get(self, request):
        data = models.Product.objects.filter(is_main=True).values(
            "id",
            "name",
            "product_detail__tag",
            "main_image_url",
            "product_detail__price",
            "product_detail__price_sale",
            "flag__flag_sale",
            "flag__flag_gift",
            "flag__flag_new",
            "flag__flag_best",
            "star_average",
        )
        reviews = (
            reviews_models.Review.objects.exclude(image_url="")
            .filter(star_point=5)
            .order_by("?")
            .values(
                "star_point", "worry__name", "skintype__name", "content", "image_url"
            )
        )[:4]
        return JsonResponse({"data": list(data), "reviews": list(reviews)}, status=200)


class AllView(View):
    def get(self, request):
        querydatas = models.Product.objects.prefetch_related("product_detail","flag")
        data = []
        for querydata in querydatas:
            data_dic = {
                "id": querydata.id,
                "name": querydata.name,
                "product_detail__tag": querydata.product_detail.tag,
                "main_image_url": querydata.main_image_url,
                "product_detail__price": querydata.product_detail.price,
                "product_detail__price_sale": querydata.product_detail.price_sale,
                "flag__flag_sale": querydata.flag.flag_sale,
                "flag__flag_gift": querydata.flag.flag_gift,
                "flag__flag_new": querydata.flag.flag_new,
                "flag__flag_best": querydata.flag.flag_best,
                "star_average": float(querydata.star_average),
                "created": str(querydata.created),
            }
            data.append(data_dic)
        return JsonResponse({"data": data}, status=200)


class DetailView(View):
    def get(self, request, pk):
        detail_pk = models.Product.objects.filter(id=pk)
        image_pk = models.Product_Detail_Image.objects.filter(product_detail_id=pk)
        images = image_pk.values("image__image_url")
        data = detail_pk.values("product_detail__detail_html")
        reviews = (
            reviews_models.Review.objects.select_related("worry", "skintype")
            .filter(product_id=pk)
            .values(
                "star_point", "worry__name", "skintype__name", "content", "image_url"
            )
        )
        return JsonResponse(
            {"images": list(images), "datas": list(data), "reviews": list(reviews)},
            status=200,
        )

# class Product_Search(View):
#     def get(self,request,searchValue):
#         search_result = models.Product.objects.filter()

class ReviewView(View):
    def get(self, request, pk):
        review_list = []
        reviews = (
            reviews_models.Review.objects.select_related("worry", "skintype")
            .filter(product_id=pk)
            .values("worry__name", "skintype__name")
        )
        qs = reviews_models.Review.objects.raw(
            """
            SELECT id,content FROM reviews
         """
        )

        for row in qs:
            print(
                ", ".join(
                    [
                        "{}: {}".format(field, getattr(row, field))
                        for field in ["id", "content"]
                    ]
                )
            )
        print(qs)
        return JsonResponse({"reviews": list(reviews)}, status=200,)
