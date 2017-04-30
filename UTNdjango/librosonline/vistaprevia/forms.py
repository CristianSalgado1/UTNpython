from django import forms

class CargarForm(forms.Form):
    producto = forms.CharField(max_length = 200)
    ruta_imagen =   forms.FileField(label = 'Selecciona un Archivo')
