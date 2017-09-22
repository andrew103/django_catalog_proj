from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from . import forms
# Create your views here.

class SignUpCustomer(CreateView):
    form_class = forms.CustomerCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup_cust.html'

class SignUpSeller(CreateView):
    form_class = forms.SellerCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup_sell.html'
