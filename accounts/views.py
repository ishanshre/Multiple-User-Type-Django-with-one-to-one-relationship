from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView

from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login

from django.core.exceptions import ValidationError


from accounts.forms import SellerCreationForm, CustomerCreationForm, SellerLoginForm
#from accounts.decorators import seller_required, customer_required
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



def loginView(request):
    return render(request, "user/login.html")

    
class SellerLoginView(SuccessMessageMixin, LoginView):
    form_class = SellerLoginForm
    template_name = "user/login_seller.html"
    success_message = "Login Successfull"

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            if user.is_authenticated and user.is_seller:
                messages.success(self.request, f"{user.username.title()}! seller login success")
                return redirect("accounts:index")
            else:
                messages.error(self.request, "This is not a seller account")
                raise ValidationError("This is not seller account")
                
        else:
            raise ValidationError("Invalid username/password")
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("accounts:index")
        return super(SellerLoginView, self).dispatch(request, *args, **kwargs)
