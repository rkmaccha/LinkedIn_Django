from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HomeView(TemplateView):
    template_name = "home/index.html"
    extra_context = {'today': datetime.today()}

# def home(request):
#     return render(request,"home/index.html",{'today': datetime.today()})

class AuthoriseView(LoginRequiredMixin,TemplateView):
    template_name = "home/authorise.html"
    login_url = '/admin'


# @login_required(login_url='/admin')
# def authorise(request):
#     return render(request,"home/authorise.html")