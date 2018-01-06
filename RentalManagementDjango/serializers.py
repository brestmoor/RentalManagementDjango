from rest_framework import serializers

from RentalManagementDjango.models import *


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Guest
        fields = '__all__'


class PlaceToRentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = PlaceToRent
        fields = '__all__'


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservation
        fields = (
            'from_date', 'to_dat', 'status', 'come_date', 'leave_date', 'advance_payment', 'no_of_people', 'person',
            'place_to_rent')
