import json

from django.views import View
from django.http import JsonResponse

from reviews import models as review_models
from products import models as product_models
from users.utils import login_decorator


class ReviewView(View):
    @login_decorator
    def post(self, request, pk):
        data = json.loads(request.body)
        try:
            worry = data["worry"]
            skintype = data["skintype"]
        except KeyError:
            worry = "없음"
            skintype = "없음"

        try:
            start_point = data["star_point"]
            content = data["content"]
        except KeyError:
            return JsonResponse({"message": "Don't find starpoint or content"}, status=400)
        try:
            product_pk = product_models.Product.objects.get(pk=pk)
            review_models.Review(
                user_id=request.user.id,
                product_id=product_pk.id,
                star_point=start_point,
                worry=review_models.Worry.objects.get(name=worry),
                skintype=review_models.SkinType.objects.get(name=skintype),
                content=content,
            ).save()
            return JsonResponse({"message": "SUCESS"}, status=200)
        except product_models.Product.DoesNotExist:
            return JsonResponse({"message": "FAIL"}, status=404)
