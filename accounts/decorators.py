"""
Creating custom decorators for protecting our login views
Here we are actually adding some changes to login required decorator.
In login required decorator it checks if user is authenticated or not
For our custom decorators we add another condition using and operator
 - for seller add additional condition that check if the user is seller
 - for customer add additional condition that check if the user is customer
"""

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def seller_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="accounts:login"):
    """
    Decorator for a login view that checks if the logged in user is a seller
    """
    actual_decorator = user_passes_test(
        lambda u:u.is_authenticated and u.is_seller,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def customer_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="accounts:login"):
    """
    Decorator for login view that checks if the logged in user is a customer
    """
    actual_decorator = user_passes_test(
        lambda u:u.is_authenticated and u.is_customer,
        login_url=login_url,
        redirect_field_name=REDIRECT_FIELD_NAME
    )
    if function:
        return actual_decorator(function)
    return actual_decorator