"""RentalManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from RentalManagementDjango.views import HelloWorld, GuestsViewSet, PlacesViewSet, ReservationsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'guests', GuestsViewSet)
router.register(r'places', PlacesViewSet)
router.register(r'reservations', ReservationsViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    path('helloWorld/', HelloWorld.as_view())
]
