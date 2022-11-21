from django.db import models 
from django.contrib.auth.models import User
# Create your models here.

class Empleado(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    documento = models.IntegerField()
    legajo = models.IntegerField()
    
    
    def __str__(self):
        return f'{self.nombre} - {self.apellido}' 

 
class Productos(models.Model):
    
    nombre = models.CharField(max_length=30)
    codigo = models.IntegerField()
    def __str__(self):
        return f'{self.nombre} - {self.codigo}'

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    documento = models.IntegerField()
    nro_cuenta = models.IntegerField()
    def __str__(self):
        return f'{self.nombre} - {self.apellido}'
    
class Avatar(models.Model):
    
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   imagen = models.ImageField(upload_to='avatares', null=True, blank=True)    