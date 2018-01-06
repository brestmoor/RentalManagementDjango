import json

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from django.views import View

from RentalManagementDjango.models import Guest, PlaceToRent
from RentalManagementDjango.serializers import PersonSerializer, PlaceToRentSerializer


class HelloWorld(View):
    def get(self, request):
        return HttpResponse(json.dumps({'Greeting': 'Hello World', 'Dog': Dog().__dict__}))


class GuestsViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = PersonSerializer


class PlacesViewSet(viewsets.ModelViewSet):
    queryset = PlaceToRent.objects.all()
    serializer_class = PlaceToRentSerializer


class Dog:
    def __init__(self):
        self.a = 'Emi'
