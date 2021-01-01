from django.urls import path
from .views import SignInView, SignUpView, BlankPageView

app_name = "observe_login"

urlpatterns = [
    path('signin/', SignInView.as_view(), name='signin'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('blank_page/', BlankPageView.as_view(), name='blank_page')
]
