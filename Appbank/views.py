from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect 

from .models import Empleado, Productos, Cliente
from .forms import ClienteFormulario,EmpleadoFormulario
from django.template import loader
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ClienteFormulario, EmpleadoFormulario, ProductoFormulario, UserEditForm, UserRegisterForm, UserCreationForm
from .models import Cliente, Productos, Empleado  #Avatar
# Create your views here.

def empleado(request, nombre, apellido, documento, legajo, empleado):
    
   empleado = Empleado(nombre=nombre, apellido=apellido, documento=documento, legajo=legajo, empleado=empleado) 
   
   empleado.save()
   
   return HttpResponse(f"""
    <p>Empleado:{empleado.nombre} - Legajo{empleado.legajo} bienvenido ! </p>
    """)
   
# def lista_personal(request):
#        # esta lo crea desde la url?
#     lista = Empleado.objects.all 
    
#     return render(request, "lista_empleados.html", {"lista_empleados": lista }) 


def inicio(request):

    return render(request,'inicio.html')
    

#def produc(request, nombre, codigo):
    
    produc = Productos(nombre=nombre, codigo=codigo) 
    
    produc.save()
   
    return HttpResponse(f"""
    <p>Producto:{produc.nombre} - codigo{produc.codigo} listo para ser usado ! </p>
    """)
    

    

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
 
def produtoFormulario(request): # crea producto 
    if request.method == 'POST':
        mi_formulario = ProductoFormulario(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            cliente = Productos(nombre=data['nombre'], codigo=data['codigo']) 
            cliente.save()  
        return redirect('/productoForm/')    
    else:  
         mi_formulario = ProductoFormulario()
    return render(request, 'productoFormulario.html', {'mi_formulario': mi_formulario})

def lista_productos(request):
    
    productos = Productos.objects.all
    contexto= {"productos" : productos}
    
    return render(request, "lista_productos.html", contexto)

def eliminarproducto(request, id): 
    if request.method == 'POST':
        productos = Productos.objects.get(id=id)    
        productos.delete()
        productos = Productos.objects.all()
        contexto= {"productos" : productos}
        
    return render(request, "lista_productos.html", contexto)


def editarproducto(request, id):  
  
    productos = Productos.objects.get(id=id)
    
    if request.method == 'POST':
        mi_formulario = ProductoFormulario(request.POST)
        
        if mi_formulario.is_valid():
        
            data = mi_formulario.cleaned_data
        
            productos.nombre = data['nombre']
            productos.codigo = data['codigo']
            
            productos.save()  
            
        return HttpResponseRedirect('/leerlistaproductos/')    
    else:  
         mi_formulario = ProductoFormulario(initial= {
            'nombre' : productos.nombre,
            'codigo': productos.codigo,
            
         })
                 
         return render(request, 'editarproducto.html', {"mi_formulario": mi_formulario, "id": productos.id})

# todo cliente funciona, crear// editar// eliminar
def clienteFormulario(request): # crea cliente
    if request.method == 'POST':
        mi_formulario = ClienteFormulario(request.POST)
        print(mi_formulario)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            cliente = Cliente(nombre=data['nombre'], apellido=data['apellido'], documento=data['documento'], nro_cuenta=data['nro_cuenta']) 
            cliente.save()  
        return redirect('/clienteForm/')    
    else:  
         mi_formulario = ClienteFormulario()
         return render(request, 'clienteFormulario.html', {'mi_formulario': mi_formulario})
     
  

def listadoclientes(request):  #lista clientes
    clientes = Cliente.objects.all()
    contexto= {"clientes" : clientes}
    return render(request, "leerclientes.html", contexto) 


def eliminarcliente(request, id): # elimina registro cliente
    if request.method == 'POST':
        clientes = Cliente.objects.get(id=id)    
        clientes.delete()
        clientes = Cliente.objects.all()
        contexto= {"clientes" : clientes}
        
    return render(request, "leerclientes.html", contexto)


def editarcliente(request, id): # edita cliente 
  
    clientes = Cliente.objects.get(id=id)
  
  
    if request.method == 'POST':
        mi_formulario = ClienteFormulario(request.POST)
        
        if mi_formulario.is_valid():
        
            data = mi_formulario.cleaned_data
        
            clientes.nombre = data['nombre']
            clientes.apellido = data['apellido']
            clientes.documento = data['documento'] 
            clientes.nro_cuenta = data['nro_cuenta'] 
            
            clientes.save()  
            
        return HttpResponseRedirect('/leerlistaclientes/')    
    else:  
         mi_formulario = ClienteFormulario(initial= {
            'nombre' : clientes.nombre,
            'apellido': clientes.apellido,
            'documento': clientes.documento, 
            'nro_cuenta': clientes.nro_cuenta,
        
         })
         
        
         return render(request, 'editarcliente.html', {"mi_formulario": mi_formulario, "id": clientes.id})
     
    

    

class EmpleadoList(LoginRequiredMixin, ListView): 
  
    model =  Empleado   
    template_name= 'lista_empleados.html' 
    context_object_name= "empleados"
    
class EmpleadoDetalle(DetailView): 
    
    model =  Empleado   
    template_name= 'detalle_empleados.html' 
    
    
class EmpleadoCrear(CreateView): 
    
    model =  Empleado   
    template_name= 'crear_empleados.html'     
    Success_url = '/Appbank/'
    
    
class EmpleadoUpdate(UpdateView): 
    
    model =  Empleado   
    template_name= 'update_empleados.html'     
    fields = ('__all__')
    success_url = '/Appbank/'
    
    
class EmpleadoDelete(DeleteView): 
    
    model =  Empleado   
    template_name= 'delete_empleados.html'             
    success_url = '/Appbank/'
    
def login_request(request):
        
    if request.method == 'POST':

        miFormulario = AuthenticationForm(request, data = request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)

            if user:

                login(request, user)

                return render(request, "inicio.html", {"mensaje": f'Bienvenido {usuario}'})
            
            else:
    
                return render(request, "inicio.html", {"mensaje": f'Error, datos incorrectos'})

        return render(request, "inicio.html", {"mensaje": f'Error, formulario invalido'})

    else:

        miFormulario = AuthenticationForm()

        return render(request, "login.html", {"miFormulario": miFormulario})

def register(request):

    print('method:', request.method)
    print('post: ', request.POST)

    if request.method == 'POST':

        miFormulario = UserRegisterForm(request.POST)

        if miFormulario.is_valid():

            username = miFormulario.cleaned_data["username"]

            miFormulario.save()

            return render(request, "inicio.html", {"mensaje": f'Usuario {username} creado con éxito'})

        else:

            return render(request, "inicio.html", {"mensaje": f'Error al crear el usuario'})

    else:

        miFormulario = UserRegisterForm()

        return render(request, "registro.html", {"miFormulario": miFormulario})


def editar_perfil(request):
    
     print('method:', request.method)
     print('post: ', request.POST)

     usuario = request.user

     if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

             data = miFormulario.cleaned_data

             usuario.first_name = data["first_name"]
             usuario.last_name = data["last_name"]
             usuario.email = data["email"]
             usuario.set_password(data["password1"])

             usuario.save()

             return render(request, "inicio.html", {"mensaje": f'Datos actualizados!'})
        
        return render(request, "editarPerfil.html", {"mensaje": 'Contraseñas no coinciden'} )
    
     else:

        miFormulario = UserEditForm(instance=request.user)

        return render(request, "editarPerfil.html", {"miFormulario": miFormulario})
    
# def about(request):
#         return render(request, "about.html")  
#         print(about)  
        