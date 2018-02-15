import json

import datetime
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, filters

# Create your views here.
from django.views import View

from RentalManagementDjango.models import Guest, PlaceToRent, Reservation, ReservationStatus
from RentalManagementDjango.serializers import PersonSerializer, PlaceToRentSerializer, ReservationSerializer, \
    ReservationStatusSerializer


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
    serializer_class = ReservationSerializer

    def get_queryset(self):
        from_date_req = self.request.query_params.get('from_date', None)
        to_date_req = self.request.query_params.get('to_date', None)
        place_to_rent_id_req = self.request.query_params.get('place_to_rent_id', None)

        if from_date_req and to_date_req and place_to_rent_id_req:
            return Reservation.objects.filter(
                Q(place_to_rent__id=place_to_rent_id_req),
                Q(Q(
                    Q(from_date__range=[from_date_req, to_date_req]) |
                    Q(to_date__range=[from_date_req, to_date_req])) |
                  Q(Q(from_date__lte=from_date_req), Q(to_date__gte=to_date_req))
                  )
            )
        else:
            return Reservation.objects.all()


class ReservationStatusViewSet(viewsets.ModelViewSet):
    queryset = ReservationStatus.objects.all()
    serializer_class = ReservationStatusSerializer


class Dog:
    def __init__(self):
        self.a = 'Emi'
