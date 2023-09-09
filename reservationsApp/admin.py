from django.contrib import admin
from .models import Reservation
# Register your models here.

class ReservationAdmin(admin.ModelAdmin):
    readonly_fields = ('dateOfReservation',)
    list_display = ("guestName", "dateFrom", "dateTo", "bNumber",)

admin.site.register(Reservation, ReservationAdmin)