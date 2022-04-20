from django.urls import path
from exemplar import views

urlpatterns = [
    path('', views.index, name='index'),
]