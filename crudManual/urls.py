"""crudManual URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import PersonaAPI, PersonaDetail,SalonesAPI, SalonesDetail, Extra, PersonaListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/1.0/personas', PersonaAPI.as_view(), name = "personas"),
    path('api/1.0/personas/<int:persona_id>', PersonaDetail.as_view(), name = "personasdetail"),
    path('api/1.0/salones', SalonesAPI.as_view(), name = "salones"),
    path('api/1.0/salones/<int:salon_id>', SalonesDetail.as_view(), name = "salonesdetail"),
    path('api/1.0/person', PersonaListView.as_view(), name = "pperson"),
]
