from django import forms

class ClienteFormulario(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    nro_cuenta = forms.IntegerField ()
    documento = forms.IntegerField()
    
    
class EmpleadoFormulario(forms.Form):
        
     nombre = forms.CharField()
     apellido = forms.CharField()
     nro_legajo = forms.IntegerField ()
     documento = forms.IntegerField()
    
    
class ProductoFormulario(forms.Form):
        
     nombre = forms.CharField()
     codigo = forms.IntegerField ()
    