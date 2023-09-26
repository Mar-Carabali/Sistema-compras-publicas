from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('analisis', views.analisis, name='analisis'),
    path('contrato', views.contrato, name='contrato'),
    path('premio', views.premio, name='premio'),
    path('planificacion', views.planificacion, name='planificacion'),
    path('lanzamiento', views.lanzamiento, name='lanzamiento'),
    path('licitacion', views.licitacion, name='licitacion'),
    path('provedores', views.provedores, name='provedores'),



    
]
