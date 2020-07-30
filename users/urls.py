from django.urls import path
from .views import SignUp, SignIn, Activate,GoogleLogin,kakao_callback

urlpatterns =[
    path('signup', SignUp.as_view()),
    path('signin', SignIn.as_view()),
    path('signin/google', GoogleLogin.as_view()),
    path("signin/kakao/callback", kakao_callback, name="kakao_callback"),
    path('activate/<str:uidb64>/<str:token>', Activate.as_view())
]