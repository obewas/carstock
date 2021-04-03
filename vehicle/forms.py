from django.forms import ModelForm
from .models import Car, Cost

class CarCreationForm(ModelForm):
    model = Car

class CostCreationForm(ModelForm):
    class Meta:
        model = Cost
        fields = '__all__'


