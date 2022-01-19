from django.urls import path

from . import views

urlpatterns = [
    # /catalog/
    path('', views.index, name='index'),
]
