from django.db import models

from core import models as core_models


class Menu(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "menus"

    def __str__(self):
        return self.name


class Skin_Category(models.Model):
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "skin_category"

    def __str__(self):
        return self.name


class Genre_Category(models.Model):
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "genre_category"

    def __str__(self):
        return self.name


class Line_Category(models.Model):
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "line_category"

    def __str__(self):
        return self.name


class Online_Category(models.Model):
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "online_category"

    def __str__(self):
        return self.name


class Product_Plag(models.Model):
    flag_sale = models.CharField(max_length=10)
    flag_gift = models.CharField(max_length=10)
    flag_new = models.CharField(max_length=10)
    flag_best = models.CharField(max_length=10)

    class Meta:
        db_table = "product_flag"

    def __str__(self):
        return self.name


class Image(models.Model):
    image_url = models.TextField(max_length=1000)

    class Meta:
        db_table = "image"


class Product_Detail_Image(models.Model):
    product_detail = models.ForeignKey(
        "Product_Detail", on_delete=models.CASCADE, null=True
    )
    image = models.ForeignKey("Image", on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "product_detail_image"

    def __str__(self):
        return f"{self.product_detail}-{self.image}"


class Product(core_models.TempDate):
    skin = models.ForeignKey("Skin_Category", on_delete=models.CASCADE, null=True)
    genre = models.ForeignKey("Genre_Category", on_delete=models.CASCADE, null=True)
    line = models.ForeignKey("Line_Category", on_delete=models.CASCADE, null=True)
    online = models.ForeignKey("Online_Category", on_delete=models.CASCADE, null=True)
    flag = models.ForeignKey("Product_Plag", on_delete=models.CASCADE, null=True)
    product_detail = models.ForeignKey(
        "Product_Detail", on_delete=models.CASCADE, null=True
    )
    star_average = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    name = models.CharField(max_length=100)
    main_image_url = models.CharField(max_length=1000, default="")
    is_main = models.BooleanField(default=False)

    class Meta:
        db_table = "products"

    def __str__(self):
        return self.name


class Distinct_Product(core_models.TempDate):
    skin = models.ForeignKey("Skin_Category", on_delete=models.CASCADE, null=True)
    genre = models.ForeignKey("Genre_Category", on_delete=models.CASCADE, null=True)
    line = models.ForeignKey("Line_Category", on_delete=models.CASCADE, null=True)
    online = models.ForeignKey("Online_Category", on_delete=models.CASCADE, null=True)
    flag = models.ForeignKey("Product_Plag", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "non_products"

    def __str__(self):
        return self.name


class Product_Detail(core_models.TempDate):
    tag = models.CharField(max_length=100)
    price = models.IntegerField()
    price_sale = models.IntegerField()
    detail_html = models.TextField(max_length=1000)

    class Meta:
        db_table = "product_detail"

    def __str__(self):
        return self.tag
