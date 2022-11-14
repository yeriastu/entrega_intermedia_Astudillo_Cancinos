from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect 

from .models import Empleado, Productos, Cliente
from .forms import ClienteFormulario,EmpleadoFormulario
from django.template import loader

# Create your views here.

def empleado(request, nombre, apellido, documento, legajo):
    
   empleado = Empleado(nombre=nombre, apellido=apellido, documento=documento, legajo=legajo) 
   
   empleado.save()
   
   return HttpResponse(f"""
    <p>Empleado:{empleado.nombre} - Legajo{empleado.legajo} bienvenido ! </p>
    """)
   
def lista_personal(request):
       # esta lo crea desde la url?
    lista = Empleado.objects.all 
    
    return render(request, "lista_empleados.html", {"lista_empleados": lista }) 


def inicio(request):

    return render(request,'inicio.html')
    

def produc(request, nombre, codigo):
    
    produc = Productos(nombre=nombre, codigo=codigo) 
    
    produc.save()
   
    return HttpResponse(f"""
    <p>Producto:{produc.nombre} - codigo{produc.codigo} listo para ser usado ! </p>
    """)
    
def lista_productos(request):
    
    lista = Productos.objects.all
    
    return render(request, "lista_productos.html", {"lista_productos": lista})
    

def cliente(request, nombre, apellido, documento, nro_cuenta):
     
   cliente = Cliente(nombre=nombre, apellido=apellido, documento=documento, nro_cuenta=nro_cuenta) 
   
   cliente.save()
   
   return HttpResponse(f"""
    <p>Cliente:{cliente.nombre} - nro_cuenta{cliente.nro_cuenta} bienvenido ! </p>
    """)
   
# def lista_cli(request):
#     lista = Cliente.objects.all 
#     return render(request, "lista_clientes.html", {"lista_cli": lista })
                 
def empleadoFormulario(request):
     
    return render(request, 'empleadoFormulario.html', )
 
def produtoFormulario(request):
     
    return render(request, 'productoFormulario.html' )
 
def clienteFormulario(request):
    if request.method == 'POST':
        mi_formulario = ClienteFormulario(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            cliente = Cliente(nombre=data['nombre'], apellido=data['apellido'], documento=data['documento'], nro_cuenta=data['nro_cuenta']) 
            cliente.save()  
        return redirect('ClienteFormulario')    
    else:  
         mi_formulario = ClienteFormulario()
         return render(request, 'clienteFormulario.html', {'mi_formulario': mi_formulario})
     
  

def listadoclientes(request):
    clientes = Cliente.objects.all()
    contexto= {"clientes" : clientes}
    return render(request, "leerclientes.html", contexto) 


def eliminarcliente(request, id):
    if request.method == 'POST':
        clientes = Cliente.objects.get(id=id)    
        clientes.delete()
        clientes = Cliente.objects.all()
        contexto= {"clientes" : clientes}
        
    return render(request, "leerclientes.html", contexto)


def editarcliente(request,id):
    clientes = Cliente.objects.get(id=id)
    
    if request.method == 'POST':
        mi_formulario = ClienteFormulario(request.POST)
        
        if mi_formulario.is_valid():
        
            data = mi_formulario.cleaned_data
        
            cliente.nombre = data['nombre'],
            cliente.apellido=data['apellido'],
            cliente.documento=data['documento'], 
            cliente.nro_cuenta=data['nro_cuenta'] 
        
            cliente.save()  
        return HttpResponseRedirect('/Appbank/')    
    else:  
         mi_formulario = ClienteFormulario(initial= {
            'nombre' : cliente.nombre,
            'apellido': cliente.apellido,
            'documento': cliente.documento, 
            'nro_cuenta': cliente.nro_cuenta,
         })
         return render(request, 'editarcliente.html', {'mi_formulario': mi_formulario, "id":cliente.id})
     
    

def crear_empleado(request):
    if request.method == 'POST':
         mi_formulario = EmpleadoFormulario(request.POST)
         print(mi_formulario)
         if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            empleado = Empleado(nombre=data['nombre'], apellido=data['apellido'], documento=data['documento'], nro_legajo=data['nro_legajo']) 
            empleado.save()  
            
         return redirect('EmpleadoFormulario')    
    else:  
         mi_formulario = EmpleadoFormulario()
         return render(request, 'empleadoFormulario.html', {'mi_formulario': mi_formulario})
     
# listado de empleados ya esta mas arriba lista_personal

