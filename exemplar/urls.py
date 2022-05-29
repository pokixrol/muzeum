from django.urls import path
from exemplar import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exemplare/', views.ExemplarListView.as_view(), name='exemplare'),
    path('easteregg/', views.easteregg, name='easteregg'),
]