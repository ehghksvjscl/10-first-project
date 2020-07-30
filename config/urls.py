from django.urls import path, include

urlpatterns = [
    path("product/", include("products.urls")),
    path("product/", include("reviews.urls")),
    path("user/", include("users.urls")),
    path("user/", include("orders.urls")),
]
