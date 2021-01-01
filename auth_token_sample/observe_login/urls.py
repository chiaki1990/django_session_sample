from django.urls import path
from .views import SignInAPIView, SignUpAPIView, BlankPageAPIView

app_name = "observe_login"

urlpatterns = [
    path('signin/', SignInAPIView.as_view(), name='signin'),
    path('signup/', SignUpAPIView.as_view(), name='signup'),
    path('blank_page/', BlankPageAPIView.as_view(), name='blank_page')
]
