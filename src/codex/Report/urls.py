from django.urls import path
from .import views
urlpatterns = [
        path('', views.home,name='website-home'),
        path('report/new/', views.CreateReport, name='report-create'),
        path('about/', views.about, name='about'),
        path('contact/', views.contact, name='contact-form'),
        path('news/', views.news, name='news'),
]
