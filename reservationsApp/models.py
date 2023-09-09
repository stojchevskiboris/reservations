from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Reservation(models.Model):
    class Types(models.TextChoices):
        Bungalov = "Bungalov", "Бунгалов"
        Prikolka = "Prikolka", "Приколка"
        Shator = "Shator", "Шатор"

    class Statuses(models.TextChoices):
        Avansirana = "Avansirana", "Авансирана"
        Zavrshena = "Zavrshena", "Завршена"
        Nova = "Nova", "Нова"
        Prioritetna = "Prioritetna", "Приоритетна"
        VoTek = "Vo tek", "Во тек"

    guestName = models.CharField(max_length=100)
    guestEmail = models.CharField(max_length=100, blank=True, null=True)
    numGuests = models.CharField(max_length=20,blank=True, null=True)
    guestPhone = models.CharField(max_length=20, null=True, blank=True)
    dateFrom = models.DateField(blank=True, null=True)
    dateTo = models.DateField(blank=True, null=True)
    type = models.CharField(max_length=12, choices=Types.choices, default=Types.Bungalov)
    bNumber = models.CharField(max_length=20,blank=True, null=True)
    resDetails = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    dateOfReservation = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=Statuses.choices, default=Statuses.Nova)
    madeBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
