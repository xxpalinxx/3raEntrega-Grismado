from django import forms

class UsuarioForm(forms.Form):
    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=60)
    email = forms.EmailField()
    edad = forms.IntegerField()


class ProyectosForm(forms.Form):
    nombre = forms.CharField(max_length=60)
    tipo = forms.CharField(max_length=60)
    comercial = forms.CharField(max_length=60)


class ConsultaForm(forms.Form):
    nombre = forms.CharField(max_length=60)
    email = forms.EmailField()
    consulta = forms.CharField(max_length=200)
