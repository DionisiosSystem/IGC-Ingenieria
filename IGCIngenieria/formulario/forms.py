from django import forms
import formulario.models

class ContactoForm(forms.ModelForm):

    class Meta:
        model = formulario.models.Contacto
        fields = '__all__'


