# Generated by Django 4.0.4 on 2022-06-04 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_passenger'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Passenger',
            new_name='Passengers',
        ),
    ]