"""ecosalud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from Inicio.views import *
#from Migraciones.views import migracion_dep, migracion_prestadores, migracion_det_prestador

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='inicio'),
    path('success/',registro,name='registro'),
    path('login/',loginView,name='login'),
    path('logout/',logoutView,name='logout'),


    path('myaccount/',micuenta,name='myaccount'),

    # path('migracion/dep',migracion_dep),
    # path('migracion/pres',migracion_prestadores),
    # path('migracion/pres/det/',migracion_det_prestador)
    #path('migracion/dep',migracion_dep),
    #path('migracion/pres',migracion_prestadores),
    #path('migracion/pres/det/',migracion_det_prestador)
]
