from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class IndexView(TemplateView):
    template_name = "page/index.html"


class ProfileView(TemplateView):
    template_name = "page/profile.html"
