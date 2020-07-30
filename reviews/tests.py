import json

from reviews import models as review_models
from products import models as product_models
from django.test import TestCase
from django.test import Client
from django.urls import reverse


class ReviewUploadlTest(TestCase):
    def setUp(self):
        client = Client()
        product_models.Menu.objects.create(id=1, name="제품")
        product_models.Skin_Category.objects.create(
            id=1, menu=product_models.Menu.objects.get(id=1), name="회복진정"
        )
        review_models.SkinType(name="없음").save()
        review_models.SkinType(name="건성").save()
        review_models.SkinType(name="지성").save()
        review_models.SkinType(name="복합성").save()
        review_models.Worry(name="없음").save()
        review_models.Worry(name="칙칙함").save()
        review_models.Worry(name="건조함").save()
        review_models.Worry(name="민감성").save()
        review_models.Worry(name="트러블").save()
        review_models.Worry(name="모공").save()
        review_models.Worry(name="노화").save()

        product_models.Product.objects.create(
            id=1,
            skin=product_models.Skin_Category.objects.get(id=1),
            star_average=5.0,
            name="스킨케어 블루샷",
            main_image_url="",
            is_main=True,
        )

    def tearDown(self):
        review_models.Review.objects.all().delete()

    def test_review_post_success(self):
        client = Client()
        author = {
            "worry": "트러블",
            "skintype": "없음",
            "content": "review 테스트2",
            "star_point": 5,
        }
        response = client.post(
            reverse("reviews", kwargs={"pk": 1}),
            json.dumps(author),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "SUCESS"})

    def test_review_post_fail(self):
        client = Client()
        author = {
            "content": "내용 입력 칸",
            "star_point": 5,
            "worry": "없음",
            "skintype": "없음",
        }
        response = client.post("/product/detail/review/edit/1ads",
                               json.dumps(author), content_type="application/json")

        self.assertEqual(response.status_code, 404)

    def test_review_post_invalid_content(self):
        client = Client()
        author = {
            "star_point": 5,
            "worry": "없음",
            "skintype": "없음",
        }
        response = client.post(
            "/product/detail/review/edit/1",
            json.dumps(author),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(), {"message": "Don't find starpoint or content"}
        )

    def test_review_post_invalid_point(self):
        client = Client()
        author = {
            "content": "내용 입력 칸",
            "worry": "없음",
            "skintype": "없음",
        }
        response = client.post(
            "/product/detail/review/edit/1",
            json.dumps(author),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json(), {"message": "Don't find starpoint or content"}
        )
