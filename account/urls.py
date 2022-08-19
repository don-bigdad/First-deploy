from django.urls import path
from .views import login_user,logout_user,registration_user

app_name = "account"

urlpatterns=[
    path("login/",login_user,name="login"),
    path("logout/",logout_user,name="logout"),
    path("registration/",registration_user,name="registration"),
    path("",login_user,name="login"),

]