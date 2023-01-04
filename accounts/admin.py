from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model as User

from accounts.forms import CustomUserChangeForm, CustomUserCreationForm
from accounts.models import Seller, Customer

# Register your models here.
@admin.register(User())
class UserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ['username','email','is_staff','is_seller','is_customer']
    fieldsets = BaseUserAdmin.fieldsets + (
        (
            "Additional Info", {
                "fields":("is_seller","is_customer")
            }
        ),
    )
    add_fieldsets = (
        (
            "Create User",
            {
                "classes": ("wide",),
                "fields": ("username","email","password1","password2"),
            }
        ),
    )


admin.site.register(Seller)
admin.site.register(Customer)