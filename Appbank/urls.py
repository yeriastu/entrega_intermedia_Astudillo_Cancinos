from django.urls import path
from Appbank import views



from django.urls import path, include
from Appbank.views import empleado, lista_productos, cliente, clienteFormulario, empleadoFormulario, produtoFormulario
from .views import empleado, lista_personal, inicio, produc, listadoclientes, eliminarcliente,editarcliente

urlpatterns = [
    path('', inicio),
    path('agrego-empleado/<nombre>/<apellido>/<documento>/<legajo>/', empleado), 
    path('lista_empleados/', lista_personal, name="Empleados"),
    path('nuevoproducto/<nombre>/<codigo>/', produc), 
    path('lista_productos/', lista_productos, name="Productos"),
    path('agrego-cliente/<nombre>/<apellido>/<documento>/<nro_cuenta>/', cliente), 
   #path('lista_clientes/', lista_cli, name="Clientes"),
    path('clienteForm/', clienteFormulario, name="ClienteFormulario"),
    path('empleadoForm/', empleadoFormulario, name="EmpleadoFormulario"),
    path('productoForm/', produtoFormulario, name="ProductoFormulario"),
    path('leerlistaclientes/', listadoclientes, name="listaclientes"),
    path('elimina-clientes/<int:id>', eliminarcliente, name="EliminaCliente"),
    path('edita-clientes/<int:id>', editarcliente, name="EditarCliente"),
    
    ]