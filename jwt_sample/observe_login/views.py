from django.shortcuts import render
from rest_framework.authtoken.views import Response, APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .serializers import UserModelSerializer
from django.contrib.auth import authenticate

# Create your views here.


class SignInAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # ログインデータテンプレートを表示する
        return Response({'username': '', 'password': ''})

    def post(self, request, *args, **kwargs):
        ''' ユーザー認証した場合にはtokenを返す '''
        username = request.data['username']
        password = request.data['password']
        print(username, password)
        user_obj = authenticate(username=username, password=password)
        if user_obj is None:
            return Response({'result': 'credential is not valid'})
        try:
            # クライアントにセットするためtokenを出力する
            token = Token.objects.get(user=user_obj.id)
            return Response({"result": "success", 'tokenKey': token.key})
        except:
            return Response({'result': 'token fail'})


class SignUpAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # 送信データテンプレートを表示する
        return Response(data={'username': '', 'password': ''}, status=200)

    # User登録と同時に当該UserにTokenをセット、発行する
    def post(self, request, *args, **kwargs):
        serializer = UserModelSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"result": "fail"})
        username = serializer.validated_data['username']
        password = serializer.validated_data["password"]
        user_obj = User.objects.create_user(
            username=username, password=password)
        token = Token.objects.create(user=user_obj)
        print("TOKEN KEY : ", token.key)
        # クライアントにセットするためtokenを出力する
        return Response({"result": "success", "tokenKey": token.key})

        """リクエストボディサンプル
        {
            "username": "test",
            "password": "password"
        }
        """


class BlankPageAPIView(APIView):

    def get(self, request, *args, **kwargs):
        # request.session["my_session_key"] = "value"
        # htmlに{% csrf_token %}が含まれて、初めて csrf_tokenがクッキーに登録される!!
        # return render(request, 'observe_login/blank_page.html')
        return Response({})
