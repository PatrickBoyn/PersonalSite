from django.urls import path
from website import views

app_name = 'website'

urlpatterns =[
path('success/', views.SuccessView.as_view(), name='success'),
]
