from django.shortcuts import render,redirect
from django.contrib import auth
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
class signup(CreateView):
	form_class = loginForm
	
	
	success_url = reverse_lazy('loginapp:login')
	template_name = 'signup.html'

  