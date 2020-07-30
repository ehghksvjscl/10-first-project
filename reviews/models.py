from django.db import models
from core import models as core_models
from products import models as products_models
from . import models as review_models


class Worry(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "worries"

    def __str__(self):
        return self.name


class SkinType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "skintypes"

    def __str__(self):
        return self.name


class Review(core_models.TempDate):
    user = models.ForeignKey('users.Users',on_delete=models.CASCADE,null=True)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, null=True)
    star_point = models.IntegerField(default=0)
    worry = models.ForeignKey(
        "Worry", on_delete=models.CASCADE, null=True
    )
    skintype = models.ForeignKey("SkinType", on_delete=models.CASCADE, null=True)
    content = models.TextField(max_length=1000)
    image_url = models.TextField(max_length=255)

    class Meta:
        db_table = "reviews"

    def __str__(self):
        return self.content
