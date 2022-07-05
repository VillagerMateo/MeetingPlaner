from datetime import date
from django.forms import ModelForm
from .models import Meeting, Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'