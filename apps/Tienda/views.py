from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

import os

# Create your views here.


def cargarInicio(request):
    return render(request,"inicio.html")


def cargarFormulario(request):
    categorias  = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request,"formulario.html",{"categ":categorias, "produc":productos})


def agregarProducto(request):
    print(request.POST)
    valor_sku = request.POST['txtSku']
    valor_nombre = request.POST['txtNombre']
    valor_precio = request.POST['txtPrecio']
    valor_cantidad = request.POST['txtStock']
    valor_categoria = Categoria.objects.get(id_categoria = request.POST['cmbCategoria'])
    valor_img = request.FILES['txtImg']

    Producto.objects.create(
        id_producto = valor_sku , 
        nombre_producto = valor_nombre , 
        precio_producto = valor_precio, 
        cantidad_producto = valor_cantidad,
        categoria_id = valor_categoria,
        imagen= valor_img)       
    
    return redirect('/formulario')




def cargarEditarProducto(request,id):

    producto = Producto.objects.get(id_producto = id)
    categorias = Categoria.objects.all()


    categoriaId = producto.categoria_id

    productoCategoriaId = Categoria.objects.get(id_categoria = categoriaId.id_categoria).id_categoria

    return render(request,"editarFormulario.html",{"produc":producto,"categ":categorias, "categoriaId":productoCategoriaId})






def editarProducto(request):
    valor_sku = request.POST['txtSku']
    productoBD = Producto.objects.get(id_producto = valor_sku)
    valor_nombre = request.POST['txtNombre']
    valor_precio = request.POST['txtPrecio']
    valor_cantidad = request.POST['txtStock']
    valor_categoria = Categoria.objects.get(id_categoria = request.POST['cmbCategoria'])

    try:
        valor_img = request.FILES['txtImg']
        ruta_imagen  = os.path.join(settings.MEDIA_ROOT, str(productoBD.imagen))
        os.remove(ruta_imagen)
    except:
        valor_img = productoBD.imagen


    productoBD.nombre = valor_nombre
    productoBD.precio = valor_precio
    productoBD.stock = valor_cantidad
    productoBD.categoria_id = valor_categoria
    productoBD.imagen = valor_img

    productoBD.save()


    return redirect('/formulario')



def eliminarProducto(request,id):
    producto = Producto.objects.get(id_producto = id)
    producto.delete()
    ruta_imagen  = os.path.join(settings.MEDIA_ROOT, str(producto.imagen))
    os.remove(ruta_imagen)

    return redirect('/formulario')



def cargarCuadernos(request):
    cuadernos = Producto.objects.filter(categoria_id=1)
    return render(request,"cuadernos.html", {"cuadernos":cuadernos})

def cargarPlanner(request):
    planner = Producto.objects.filter(categoria_id=2)
    return render(request,"planers.html", {"planers":planner})

def cargarMarca(request):
    marcaPag = Producto.objects.filter(categoria_id=3)
    return render(request,"marcaPagina.html", {"marca":marcaPag})



def cargarRegistro(request):

    if request.method == 'GET':
            return render(request,"registro.html", {
            'form': UserCreationForm
    })

    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return redirect('/login')
            
            except IntegrityError:
                return render(request,"registro.html", {
                'form': UserCreationForm,
                'error': 'El usuario ya existe'
                })
        
        return render(request,"registro.html", {
            'form': UserCreationForm, 
            'error' : 'Las contraseñas no son iguales'
            })

def cargarLogin(request):
    if request.method == 'GET':
        return render(request,"login.html", {
        'form': AuthenticationForm
    })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request,"login.html", {
            'form': AuthenticationForm,
            'error': 'Usuario o contraseña incorrecta'
             })
        else:
            login(request,user)
            return redirect('/')

    





def cerrarSesion(request):
    logout(request)
    return redirect('/')


