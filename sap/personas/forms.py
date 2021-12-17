from django.forms import ModelForm, widgets, TextInput
from personas.models import Persona, Domicilio


#--- Formulario para agregar personas ---#
class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'email': widgets.EmailInput(attrs={'type':'email'}),
            
        }

