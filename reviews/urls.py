from django.urls import path

from . import views

urlpatterns = [
    path("detail/review/edit/<int:pk>", views.ReviewView.as_view(), name="reviews"),
]
