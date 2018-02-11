import json

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, filters

# Create your views here.
from django.views import View

from RentalManagementDjango.models import Guest, PlaceToRent, Reservation
from RentalManagementDjango.serializers import PersonSerializer, PlaceToRentSerializer, ReservationSerializer


class HelloWorld(View):
    def get(self, request):
        return HttpResponse(json.dumps({'Greeting': 'Hello World', 'Dog': Dog().__dict__}))


class GuestsViewSet(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = PersonSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('^name', '^surname')


class PlacesViewSet(viewsets.ModelViewSet):
    queryset = PlaceToRent.objects.all()
    serializer_class = PlaceToRentSerializer


class ReservationsViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class Dog:
    def __init__(self):
        self.a = 'Emi'
