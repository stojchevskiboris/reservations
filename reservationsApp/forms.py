from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Reservation
        fields = '__all__'
        # exclude = ("dateOfReservation",)