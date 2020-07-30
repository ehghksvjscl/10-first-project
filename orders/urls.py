from django.urls import path

from . import views

urlpatterns = [
    path("orderadd", views.CartAddView.as_view(), name="orderadd"),
    path("orderminus", views.CartMinusView.as_view(), name="orderminus"),
    path("orderdelete", views.CartDeletView.as_view(), name="orderdelete"),
    path("order", views.CartList.as_view(), name="order"),
]
