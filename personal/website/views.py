from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'


class PortfolioView(TemplateView):
    template_name = 'portfolio.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class AboutView(TemplateView):
    template_name = 'about.html'
