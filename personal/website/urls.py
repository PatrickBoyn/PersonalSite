from django.urls import path
from website import views


urlpatterns =[
path('contact/success', views.SuccessView),
]
