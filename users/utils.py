import DBConnent
import jwt

from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from users import models 


def login_decorator(func):
    def wrapper(self,request,*args, **kwargs):
        if "Authorization" not in request.headers:
            return JsonResponse({"message":"INALID_LOGIN"},status=401)
        token = request.headers["Authorization"]
        try:
            user_token = jwt.decode(token,DBConnent.SECRET,algorithm='HS256')
            user = models.Users.objects.get(id=user_token["user"])
            request.user = user

        except jwt.DecodeError:
            return JsonResponse({"message":"INVALID TOKEN"},status=401)

        except models.Users.DoesNotExist:
            return JsonResponse({"message":"NOT EXITST USER"},status=401)

        return func(self,request, *args, **kwargs)
    return wrapper

class DecoratorView(View):
    @login_decorator
    def get(self,request):
        print(dir(request.user.id))
        return JsonResponse({"message":f"{request.user.email}님 환영 합니다."})