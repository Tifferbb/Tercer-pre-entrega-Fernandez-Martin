from django import forms
from .models import Nutricionista, Paciente, Sesion

class NutricionistaForm(forms.ModelForm):
    class Meta:
        model = Nutricionista
        fields = '__all__'

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

class SesionForm(forms.ModelForm):
    class Meta:
        model = Sesion
        fields = '__all__'
