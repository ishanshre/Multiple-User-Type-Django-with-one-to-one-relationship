from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import get_user_model
from django.contrib import messages

from accounts.forms import SellerCreationForm, CustomerCreationForm
# Create your views here.
User = get_user_model()

def index(request):
    return render(request, "index.html")

def register(request):
    return render(request, "user/register.html")

class SellerRegsiterView(CreateView):
    model = User
    form_class = SellerCreationForm
    template_name = "user/sellerRegister.html"

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'seller'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, "Seller Created")
        return redirect("accounts:index")


class CustomerRegisterView(CreateView):
    model = User
    form_class = CustomerCreationForm
    template_name = "user/customerRegister.html"

    def get_context_data(self, **kwargs):
        kwargs['user_type']='customer'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, "Customer Created")
        return redirect("accounts:index")
