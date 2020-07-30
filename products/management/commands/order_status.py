from django.core.management.base import BaseCommand, no_translations
from orders import models as order_models
import csv


class Command(BaseCommand):
    @no_translations
    def handle(self, *args, **options):
        order_models.OrderStatus(name="장바구니").save()
        order_models.OrderStatus(name="주문접수").save()
        order_models.OrderStatus(name="결제완료").save()
        order_models.OrderStatus(name="배송준비중").save()
        order_models.OrderStatus(name="배송중").save()
        order_models.OrderStatus(name="배송완료").save()
        order_models.OrderStatus(name="주문완료").save()
