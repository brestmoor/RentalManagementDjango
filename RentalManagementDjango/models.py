from django.db import models


# Create your models here.

class Guest(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    phone = models.IntegerField(null=True)
    email = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=200, null=True)
    plate_numbers = models.CharField(max_length=20, null=True)
    car = models.CharField(max_length=100, null=True)


class PlaceToRent(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    opened = models.BooleanField(default=True)
    square_m = models.IntegerField()
    color = models.CharField(max_length=200)


class ReservationStatus(models.Model):
    NOT_CONFIRMED = 'Not confirmed'
    status = models.CharField(default=NOT_CONFIRMED, max_length=20)


class Reservation(models.Model):
    CONFIRMED = 'CF'
    NOT_CONFIRMED = 'NC'
    IN_PROGRESS = 'IP'
    STATUS_CHOICES = (
        (CONFIRMED, 'Confirmed'),
        (NOT_CONFIRMED, 'Not confirmed'),
        (IN_PROGRESS, 'In progress'),
        (IN_PROGRESS, 'In progress'),
    )
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    advance_payment = models.FloatField(null=True)
    no_of_people = models.IntegerField()
    status = models.ForeignKey(ReservationStatus, on_delete=models.DO_NOTHING)
    person = models.ForeignKey(Guest, on_delete=models.CASCADE)
    place_to_rent = models.ForeignKey(PlaceToRent, on_delete=models.CASCADE)
