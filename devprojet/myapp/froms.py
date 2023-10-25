from django import forms  
from myapp.models import login  
class loginforms(forms.ModelForm):  
    class Meta:  
        model = login  
        fields = ['name', 'age','mojor','contact' ] 
        widgets = { 
            'name': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'age': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'mojor': forms.TextInput(attrs={ 'class': 'form-control' }),
            'contact': forms.NumberInput(attrs={ 'class': 'form-control' }),
      }