# Generated by Django 2.0 on 2018-02-12 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RentalManagementDjango', '0004_auto_20180212_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='placetorent',
            name='color',
            field=models.CharField(default='red', max_length=200),
            preserve_default=False,
        ),
    ]
