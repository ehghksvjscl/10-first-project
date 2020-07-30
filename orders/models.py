from django.db import models


class Order(models.Model):
    user              = models.ForeignKey('users.Users',on_delete=models.CASCADE,null=True)
    order_status      = models.ForeignKey('OrderStatus',on_delete=models.CASCADE,null=True)
    order_time        = models.DateTimeField(null=True)
    delivery_address  = models.CharField(max_length=255)
    time_canceled     = models.DateTimeField(null=True)
    time_completed    = models.DateTimeField(null=True)
    time_send         = models.DateTimeField(null=True)
    total_price       = models.IntegerField(default=0)
    disconut_price    = models.IntegerField(default=0)
    final_price       = models.IntegerField(default=0)
    active            = models.BooleanField(default=False)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return f"{self.user} - {self.order_status}"

class OrderStatus(models.Model):
    name    = models.CharField(max_length=10)

    class Meta:
        db_table = 'order_statuses'

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    order            = models.ForeignKey('Order',on_delete=models.CASCADE,null=True)
    product         = models.ForeignKey('products.Product',on_delete=models.CASCADE,null=True)
    quantity        = models.IntegerField(default=0)

    class Meta:
        db_table = 'order_items'

    def __str__(self):
        return f"{self.user} - {self.product}"