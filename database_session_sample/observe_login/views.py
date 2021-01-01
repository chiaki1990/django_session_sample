from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
# Create your views here.


class SignInView(View):
    # csrftokenとcsrftokenmiddlewareの関係性
    # https: // stackoverflow.com/questions/48002861/whats-the-relationship-between-csrfmiddlewaretoken-and-csrftoken

    def get(self, request, *args, **kwargs):
        context = {"title": "ログイン"}
        # return HttpResponse("200")
        return render(request, 'observe_login/signin.html', context)

    def post(self, request, *args, **kwargs):
        # https://djangoproject.jp/doc/ja/1.0/topics/auth.html
        username = self.request.POST["username"]
        password = self.request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("認証成功")
        else:
            return HttpResponse("認証失敗")

        return render(request, 'observe_login/signin.html')


class SignUpView(View):

    def get(self, request, *args, **kwargs):
        context = {"title": "ユーザー登録"}
        # return HttpResponse("200")
        return render(request, 'observe_login/signup.html', context)

    def post(self, request, *args, **kwargs):
        username = self.request.POST["username"]
        password = self.request.POST["password"]
        User.objects.create_user(username=username, password=password)
        return redirect(reverse("observe_login:signin"))


class BlankPageView(View):

    def get(self, request, *args, **kwargs):
        request.session["my_session_key"] = "value"
        # htmlに{% csrf_token %}が含まれて、初めて csrf_tokenがクッキーに登録される!!
        return render(request, 'observe_login/blank_page.html')
