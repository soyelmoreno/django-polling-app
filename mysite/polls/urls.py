from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wow', views.wow, name='wowpage'),
]
