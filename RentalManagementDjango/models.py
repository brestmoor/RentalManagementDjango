from django.db import models


# Create your models here.

class Guest(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    plate_numbers = models.CharField(max_length=20)
    car = models.CharField(max_length=100)


class PlaceToRent(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    opened = models.BooleanField(default=True)
    square_m = models.IntegerField()


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
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=NOT_CONFIRMED)
    come_date = models.DateTimeField()
    leave_date = models.DateTimeField()
    advance_payment = models.FloatField()
    no_of_people = models.IntegerField()

    person = models.ForeignKey(Guest, on_delete=models.CASCADE)
    place_to_rent = models.ForeignKey(PlaceToRent, on_delete=models.CASCADE)
