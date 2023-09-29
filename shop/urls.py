from django.urls import path
from shop import views

urlpatterns = [
    path('', views.Main, name="index-page"),
    path('export/', views.ExportWord, name='export'),
]