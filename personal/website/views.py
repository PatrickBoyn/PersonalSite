from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from website.forms import ContactForm
from django.urls import reverse
from django import forms


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'


class PortfolioView(TemplateView):
    template_name = 'portfolio.html'


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_message = "You've been successful!"
    # success_url = 'success/'

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class AboutView(TemplateView):
    template_name = 'about.html'


class SuccessView(TemplateView):
    template_name = 'success.html'
