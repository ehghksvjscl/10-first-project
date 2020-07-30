from django.test import TestCase
from django.test import Client

from products import models as product_models
from reviews import models as review_models

from decimal import Decimal


class ProductAllTest(TestCase):
    maxDiff = None

    def setUp(self):
        client = Client()
        product_models.Menu.objects.create(id=1, name="제품")
        product_models.Skin_Category.objects.create(
            id=1, menu=product_models.Menu.objects.get(id=1), name="회복진정")
        product_models.Skin_Category.objects.create(
            id=2, menu=product_models.Menu.objects.get(id=1), name="수분케어")
        product_models.Product_Detail.objects.create(
            id=1,
            tag="#수분케어",
            price=5000,
            price_sale=0,
            detail_html=""
        )
        product_models.Product_Plag.objects.create(
            id=1,
            flag_sale="",
            flag_gift="",
            flag_new="",
            flag_best=""
        )
        product_models.Product.objects.create(
            id=1,
            skin=product_models.Skin_Category.objects.get(id=1),
            star_average=Decimal("5.00"),
            name="스킨케어 블루샷",
            main_image_url="",
            is_main=False,
            flag=product_models.Product_Plag.objects.get(id=1),
            product_detail=product_models.Product_Detail.objects.get(id=1)
        )

    def tearDown(self):
        product_models.Product.objects.all().delete()

    def test_product_all_get_success(self):
        client = Client()
        response = client.get("/product/all")
        querydatas = product_models.Product.objects.prefetch_related("product_detail","flag")
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
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"data": data})


class ProductMainTest(TestCase):
    maxDiff = None

    def setUp(self):
        client = Client()
        product_models.Menu.objects.create(id=1, name="제품")
        product_models.Skin_Category.objects.create(
            id=1, menu=product_models.Menu.objects.get(id=1), name="회복진정")
        product_models.Skin_Category.objects.create(
            id=2, menu=product_models.Menu.objects.get(id=1), name="수분케어")
        product_models.Product_Detail.objects.create(
            id=1,
            tag="#수분케어",
            price=5000,
            price_sale=0,
            detail_html=""
        )
        product_models.Product_Plag.objects.create(
            id=1,
            flag_sale="",
            flag_gift="",
            flag_new="",
            flag_best=""
        )
        product_models.Product.objects.create(
            id=1,
            skin=product_models.Skin_Category.objects.get(id=1),
            star_average="5.00",
            name="스킨케어 블루샷",
            main_image_url="",
            is_main=True,
            flag=product_models.Product_Plag.objects.get(id=1),
            product_detail=product_models.Product_Detail.objects.get(id=1)
        )

    def tearDown(self):
        product_models.Product.objects.all().delete()

    def test_product_main_get_success(self):
        client = Client()
        response = client.get("/product/all")
        querydatas = product_models.Product.objects.prefetch_related("product_detail","flag")
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
                "star_average": querydata.star_average,
                "created": str(querydata.created),
            }
            data.append(data_dic)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"data": data})



class ProductDetailTest(TestCase):
    maxDiff = None

    def setUp(self):
        client = Client()
        product_models.Menu.objects.create(id=1, name="제품")
        product_models.Skin_Category.objects.create(
            id=1, menu=product_models.Menu.objects.get(id=1), name="회복진정")
        product_models.Skin_Category.objects.create(
            id=2, menu=product_models.Menu.objects.get(id=1), name="수분케어")
        product_models.Product_Detail.objects.create(
            id=1,
            tag="#수분케어",
            price=5000,
            price_sale=0,
            detail_html=""
        )
        product_models.Product_Plag.objects.create(
            id=1,
            flag_sale="",
            flag_gift="",
            flag_new="",
            flag_best=""
        )
        product_models.Image.objects.create(
            id=1,
            image_url = ""
        )
        product_models.Product_Detail_Image.objects.create(
            id=1,
            product_detail=product_models.Product_Detail.objects.get(id=1),
            image = product_models.Image.objects.get(id=1)
        )
        product_models.Product.objects.create(
            id=1,
            skin=product_models.Skin_Category.objects.get(id=1),
            star_average="5.00",
            name="스킨케어 블루샷",
            main_image_url="",
            is_main=True,
            flag=product_models.Product_Plag.objects.get(id=1),
            product_detail=product_models.Product_Detail.objects.get(id=1)
        )

    def tearDown(self):
        product_models.Product.objects.all().delete()

    def test_product_detail_get_success(self):
        client = Client()
        response = client.get("/product/detail/1")

        detail_pk = product_models.Product.objects.filter(id=1)
        image_pk = product_models.Product_Detail_Image.objects.filter(product_detail_id=1)
        images = image_pk.values("image__image_url")
        data = detail_pk.values("product_detail__detail_html")
        reviews = (
            review_models.Review.objects.select_related("worry", "skintype")
            .filter(product_id=1)
            .values(
                "star_point", "worry__name", "skintype__name", "content", "image_url"
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"images": list(images), "datas": list(data), "reviews": list(reviews)})
   
    def test_product_detail_get_fail(self):
        client = Client()
        response = client.get("/product/detail/strng")

        self.assertEqual(response.status_code, 404)
