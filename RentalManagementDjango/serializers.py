import datetime
from rest_framework import serializers

from RentalManagementDjango.models import *


class PersonSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Guest
        fields = '__all__'


class PlaceToRentSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = PlaceToRent
        fields = '__all__'


class ReservationSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'from_date': instance.from_date.date(),
            'to_date': instance.to_date.date(),
            'status': instance.status,
            'come_date': instance.come_date.date(),
            'leave_date': instance.leave_date.date(),
            'advance_payment': instance.advance_payment,
            'no_of_people': instance.no_of_people,
            'person': PersonSerializer(instance.person).data,
            'place_to_rent': PlaceToRentSerializer(instance.place_to_rent).data
        }

    def to_internal_value(self, data):
        return data

    def create(self, validated_data):
        person_id = validated_data['person']['id']
        if person_id:
            validated_data.pop('person')
            validated_data['person_id'] = person_id
            return self.create_new_reservation(validated_data)
        else:
            new_person = Guest.objects.create(**validated_data['person'])
            new_id = new_person.id
            validated_data.pop('person')
            validated_data['person_id'] = new_id
            return self.create_new_reservation(validated_data)

    def create_new_reservation(self, validated_data):
        new_reservation = Reservation()
        new_reservation.from_date = datetime.datetime.strptime(validated_data['from_date'], '%Y-%m-%d')
        new_reservation.to_date = datetime.datetime.strptime(validated_data['to_date'], '%Y-%m-%d')
        new_reservation.status = validated_data['status']
        new_reservation.come_date = datetime.datetime.strptime(validated_data['come_date'], '%Y-%m-%d')
        new_reservation.leave_date = datetime.datetime.strptime(validated_data['leave_date'], '%Y-%m-%d')
        new_reservation.advance_payment = validated_data['advance_payment']
        new_reservation.no_of_people = validated_data['no_of_people']
        new_reservation.person_id = validated_data['person_id']
        new_reservation.place_to_rent_id = validated_data['place_to_rent_id']
        new_reservation.save()
        return new_reservation

    def update(self, instance, validated_data):
        instance.from_date = datetime.datetime.strptime(validated_data['from_date'], '%Y-%m-%d')
        instance.to_date = datetime.datetime.strptime(validated_data['to_date'], '%Y-%m-%d')
        instance.status = validated_data['status']
        instance.come_date = datetime.datetime.strptime(validated_data['come_date'], '%Y-%m-%d')
        instance.leave_date = datetime.datetime.strptime(validated_data['leave_date'], '%Y-%m-%d')
        instance.advance_payment = validated_data['advance_payment']
        instance.no_of_people = validated_data['no_of_people']
        instance.person_id = validated_data['person_id']
        instance.place_to_rent_id = validated_data['place_to_rent_id']
        instance.save()
        return instance
