from django.shortcuts import render


from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import request
from formulario.models import Usuario, Contacto
from django.views.decorators.csrf import csrf_protect
import formulario.forms
import requests
import urllib.request, json


# Buscar Usuario
def busqueda_usuario(request):

    return render(request, "BuscarUsuarios.html")


def buscar(request):

   if request.GET["txt_nombre"]:
        mensaje = "usuario buscado: %r" %request.GET["txt_nombre"]
        # nomUsuario=request.GET["txt_nombre"]
        #
        # usuario= Usuario.objects.filter(Nombre_icontains=nomUsuario)
        # return render("resultados_busqueda.html", {"usuario":nomUsuario,"query":nomUsuario})

   else:
        mensaje = "ingrese datos"
   return HttpResponse(mensaje)

# Consumo API Externa
def home(request):
    response = requests.get('https://api.gael.cl/general/public/monedas/USD')

    geodata = response.json()


    context = locals()

    return render(request, 'index.html', {
          'Nombre': geodata['Nombre'],
          'Valor': geodata['Valor'],
          'Fecha': geodata['Fecha']
     })



# vista para guardar los datos de contacto en la base de datos
@csrf_protect
def contacto(request):
    mensaje = {'resultado': ''}
    if (request.method=="POST"):
        data = request.POST.copy()
        try:
            contacto = formulario.forms.ContactoForm(data, prefix='')
            if contacto.is_valid():
               print("es valido")
               # --- SI FORMULARIO DE ELEMENTO ES VALIDO, REGISTRA EL RESTO DE INFORMACION ---
               solicitud = contacto.save()
               mensaje = {'resultado': 'Sus datos han sido registrados con exito'}

            else:
               print("error")
               print(contacto.errors)
        except Exception as e:
            return HttpResponse("Error al ingresar el registro: " + str(e))


    return render(request, "contacto.html", mensaje )
    #return render(request, 'index.html', context))

@csrf_protect
def mensajes(request):
    listadoMensajes = None
    filtroNombre =''

    if (request.method == "POST"):
        filtroNombre=request.POST['nombre']
        listadoMensajes=formulario.models.Contacto.objects.filter(Nombre__icontains=request.POST['nombre'] )

    else:
        listadoMensajes = formulario.models.Contacto.objects.all()

    return render(request, "listadoMensajes2.html", {"listadoMensajes": listadoMensajes,"filtroNombre":filtroNombre})


def clientes(request):
    return render(request, "clientes.html")

def obrasCiviles(request):
    return render(request, "obrasCiviles.html")

def obrasMenores(request):
    return render(request, "obrasMenores.html")

def QuienesSomos(request):
    return render(request, "QuienesSomos.html")


# Codigo Mantenedor de producto
# Listar Productos
@csrf_protect
def productos(request):
    listadoProductos = None
    filtroNombre =''

    if (request.method == "POST"):
        filtroNombre=request.POST['nombre']
        listadoProductos=formulario.models.ListaPrecio.objects.filter(Nombre__icontains=request.POST['nombre'] )

    else:
        listadoProductos = formulario.models.ListaPrecio.objects.all()

    return render(request, "listadoProductos2.html", {"listadoProductos": listadoProductos,"filtroNombre":filtroNombre})
# Insertar Productos
@csrf_protect
def insertarProducto(request):
    mensaje = {'resultado': ''}
    if (request.method=="POST"):
        data = request.POST.copy()
        try:
            productos = formulario.forms.ListaPrecioForm(data, prefix='')
            if productos.is_valid():
               print("es valido")
               # --- SI FORMULARIO DE ELEMENTO ES VALIDO, REGISTRA EL RESTO DE INFORMACION ---
               solicitud = productos.save()
               mensaje = {'resultado': 'Sus datos han sido registrados con exito'}

            else:
               print("error")
               print(productos.errors)
        except Exception as e:
            return HttpResponse("Error al ingresar el registro: " + str(e))


    return render(request, "insertarProducto.html", mensaje )

# Borrar Productos
def delete(request, producto_id):        
    productos=formulario.models.ListaPrecio.objects.get(id=producto_id)
    productos.delete()
    mensaje = {'resultado': 'Registro Eliminado'}
    return render(request, "insertarProducto.html", mensaje)

# Modificar Productos
def modificar(request, producto_id):     
    # obtenemos los datos con el id del producto
    productos = get_object_or_404(formulario.models.ListaPrecio, id=producto_id) 
    # Preguntamos si viene por post 
    if request.method == 'POST':
        formu = formulario.forms.ListaPrecioForm(data=request.POST, instance=productos, files=request.FILES)
        if formu.is_valid():
            formu.save()
            return redirect(to="listadoProductos")
           
       
    return render(request, 'modificarProducto.html', {'productos': productos})





    

