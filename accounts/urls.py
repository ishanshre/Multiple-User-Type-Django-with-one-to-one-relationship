from django.urls import path
from accounts import views

app_name = "accounts"


urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("register/seller/", views.SellerRegsiterView.as_view(), name="sellerRegister"),
    path("register/customer/", views.CustomerRegisterView.as_view(), name="customerRegister"),
    
]