from django.urls import path
from accounts import views
from django.contrib.auth.views import LogoutView

app_name = "accounts"


urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("register/seller/", views.SellerRegsiterView.as_view(), name="sellerRegister"),
    path("register/customer/", views.CustomerRegisterView.as_view(), name="customerRegister"),
    path("login/", views.loginView, name='login'),
    path("sellerportal/", views.SellerLoginView.as_view(), name="sellerportal"),

    path("logout/", LogoutView.as_view(), name="logout"),
]