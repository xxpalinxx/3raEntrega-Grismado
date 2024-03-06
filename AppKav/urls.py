from django.urls import path
from AppKav.views import *

urlpatterns = [
    path("", inicio, name="Home"),
    path("registrar_usuario/", registrar_usuario, name="Registrar usuario"),
    path("ver_usuario/", ver_usuario, name="Ver usuario"),
    path("crear_proyecto/", crear_proyecto, name="Crear proyecto"),
    path("ver_proyecto/", ver_proyecto, name="Ver proyecto"),
    path("crear_consulta/", crear_consulta, name="Crear consulta"),
    path("ver_consulta/", ver_consulta, name="Ver consulta"),

]