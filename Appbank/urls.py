from django.urls import path
from Appbank import views




from django.urls import path, include
from .views import empleado, cliente, clienteFormulario, empleadoFormulario, produtoFormulario
from .views import inicio,listadoclientes, eliminarcliente, editarcliente, empleadoFormulario  #about ,  
from .views import lista_productos,editarproducto,EmpleadoList, EmpleadoDetalle, eliminarproducto, editar_perfil, register, login_request
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio),
    path('tituloproducto/', lista_productos, name="Productos"),
    path('titulocliente/', listadoclientes, name="Clientes"),
    path('tituloempleado/', EmpleadoList.as_view(),name="Empleados"),
    path('agrego-cliente/<nombre>/<apellido>/<documento>/<nro_cuenta>/', cliente), 
    path('clienteForm/', clienteFormulario, name="ClienteFormulario"),
    path('empleadoForm/', empleadoFormulario, name="EmpleadoFormulario"),
    path('productoForm/', produtoFormulario, name="ProductoFormulario"),
    path('leerlistaproductos/', lista_productos, name="listaproductos"),
    path('elimina-producto/<int:id>', eliminarproducto, name="EliminaProducto"),
    path('EditarProductos/<int:id>', editarproducto, name="EditarProducto"),
    path('leerlistaclientes/', listadoclientes, name="listaclientes"),
    path('elimina-clientes/<int:id>', eliminarcliente, name="EliminaCliente"),
    path('EditarClientes/<int:id>', editarcliente, name="EditarCliente"),
    path('detalle-Empleado/<pk>', EmpleadoDetalle.as_view(), name="Detalle-Empleado"),
    path('login/', login_request, name="Login"),
    path('registrar/', register, name="Registrar"),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="Logout"),
    path('editar-perfil/', editar_perfil, name="EditarPerfil"),
    #path('sobremi/', about),
]   


