from django.urls import path
from . import views

urlpatterns = [
    path("", views.holaDjango, name="holaDjango"),
    path('pepe', views.pepe, name='holaPepe'),
    path('<str:nombre>', views.holaTu, name='holaTu')
    ]