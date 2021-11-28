from django.contrib import admin
from django.urls import path
from .views import grafo,calculaUmbral
from . import views

#app_name = 'grafo'

urlpatterns = [

    path('grafo/',grafo,name="grafo"),
    path('calculaUmbral',calculaUmbral,name="calculaUmbral"),

    
]