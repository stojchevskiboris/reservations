# Generated by Django 4.2.2 on 2023-09-09 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guestName', models.CharField(max_length=100)),
                ('guestEmail', models.CharField(blank=True, max_length=100, null=True)),
                ('numGuests', models.CharField(blank=True, max_length=20, null=True)),
                ('guestPhone', models.CharField(blank=True, max_length=20, null=True)),
                ('dateFrom', models.DateField(blank=True, null=True)),
                ('dateTo', models.DateField(blank=True, null=True)),
                ('type', models.CharField(choices=[('Bungalov', 'Бунгалов'), ('Prikolka', 'Приколка'), ('Shator', 'Шатор')], default='Bungalov', max_length=12)),
                ('bNumber', models.CharField(blank=True, max_length=20, null=True)),
                ('resDetails', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('dateOfReservation', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Avansirana', 'Авансирана'), ('Zavrshena', 'Завршена'), ('Nova', 'Нова'), ('Prioritetna', 'Приоритетна'), ('Vo tek', 'Во тек')], default='Nova', max_length=20)),
                ('madeBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
