from django.forms import ModelForm
from .models import Record
from django.forms import ModelForm, TextInput
from datetime import date

class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ['date', 'description', 'category', 'cash', 'balance_type']
        widgets = {
            'date':TextInput(
                attrs={
                'id' : 'datepicker1',
                'value' : date.today().strftime('%Y-%m-%d')
                }
            )
        }