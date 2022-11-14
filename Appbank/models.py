from django.db import models 

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