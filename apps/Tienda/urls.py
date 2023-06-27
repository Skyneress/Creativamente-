from django.urls import path
from . import views

urlpatterns = [
    path('', views.cargarInicio),
    path('formulario',views.cargarFormulario),
    path('agregar',views.agregarProducto),
    path('editarFormulario/<id>',views.cargarEditarProducto),
    path('editar',views.editarProducto),
    path('eliminar/<id>',views.eliminarProducto),
    path('cuadernos',views.cargarCuadernos),
    path('planers',views.cargarPlanner),
    path('marca',views.cargarMarca),
    path('registro',views.cargarRegistro),
    path('login',views.cargarLogin),
    path('cerrar',views.cerrarSesion)
]