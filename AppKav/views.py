from django.shortcuts import render
from AppKav.models import *
from AppKav.forms import *

#-------------------INICIO---------------------#
def inicio(request):

    return render(request, "AppKav/inicio.html")

#-------------------USUARIO---------------------#
#CREAR

def registrar_usuario(request):

    if request.method == "POST":
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            info_dict = formulario.cleaned_data
            nuevo_usuario = Usuario(
                nombre=info_dict["nombre"],
                apellido=info_dict["apellido"],
                email=info_dict["email"],
                edad=info_dict["edad"] 
                )
            nuevo_usuario.save()
            return render(request, "AppKav/inicio.html")
    else:
        formulario = UsuarioForm()

    return render(request, "AppKav/registrar_usuario.html", {"formulario":formulario})


#VER
def ver_usuario(request):
    busqueda = request.GET.get("nombre","")
    if busqueda == "":
        return render(request, "AppKav/ver_usuario.html")
    else:
        resultado = Usuario.objects.filter(nombre__icontains=busqueda)
        return render(request, "AppKav/ver_usuario.html", {"resultado":resultado})


#-------------------PROYECTOS---------------------#
#CREAR
def crear_proyecto(request):

    return render(request, "AppKav/crear_proyecto.html")

#VER
def ver_proyecto(request):

    return render(request, "AppKav/ver_proyecto.html")


#-------------------CONSULTAS---------------------#
#CREAR
def crear_consulta(request):

    if request.method == "POST":
        formulario = ConsultaForm(request.POST)
        if formulario.is_valid():
            info_dict = formulario.cleaned_data
            nueva_consulta = Consulta(
                nombre=info_dict["nombre"],
                email=info_dict["email"],
                consulta=info_dict["consulta"]
                )
            nueva_consulta.save()
            return render(request, "AppKav/inicio.html")
    else:
        formulario = ConsultaForm()

    return render(request, "AppKav/crear_consulta.html", {"formulario":formulario})

#VER
def ver_consulta(request):
    busqueda = request.GET.get("nombre","")
    if busqueda == "":
        return render(request, "AppKav/ver_consulta.html")
    else:
        resultado = Consulta.objects.filter(nombre__icontains=busqueda)
        return render(request, "AppKav/ver_consulta.html", {"resultado":resultado})
    