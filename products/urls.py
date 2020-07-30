from django.urls import path

from . import views

urlpatterns = [
    path("main", views.MainView.as_view()),
    path("all", views.AllView.as_view()),
    path("detail/<int:pk>", views.DetailView.as_view()),
    path("detail/review/<int:pk>", views.ReviewView.as_view()),
]
