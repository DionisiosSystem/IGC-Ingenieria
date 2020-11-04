from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.http import request
from formulario.models import Usuario, Contacto
from django.views.decorators.csrf import csrf_protect
import formulario.forms

# Create your views here.
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


def home(request):
    return render(request, "index.html")

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



