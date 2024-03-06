# 3raEntrega-Grismado


## ALVAR Arquitectura - Pagina Web

Pagina web en desarrollo con el fin de crear y ver usuarios, consultas y proyectos de arquitectura

### Instalacion requerida
Para ver este proyecto es necesario tener instalado Django y en un principio ejecutar las siguientes lineas de codigo para evitar posibles errores.


1- Para asegurarnos que se cree la base de datos en donde haremos la interaccion:

*windows*
```bash
  python manage.py makemigrations 
```
```bash
  python manage.py migrate 
``` 
*MacOS*
```bash
  python3 manage.py makemigrations 
```
```bash
  python3 manage.py migrate 
``` 

2- Para ejecutar el servidor que nos permitirá ver la pagina en un navegador habra que ejecutar el siguiente codigo:
*windows*
```bash
  python manage.py runserver 
```
*MacOS*
```bash
  python3 manage.py runserver
```

Para acceder a la pagina en el navegador se debe escribir la siguiente url:
```bash
  localhost:8000/ 
```
Esto mostrara disponible dos Apps, la correspondiente a la seccion de admin y a la App de la pagina en desarrollo.
### Admin Page
Se puede acceder a la pagina de admin mediante la url:
```bash
  localhost:8000/admin
```
Los datos necesarios para loguearse como administrador y realizar las pruebas pertinentes son:

_user_: karladmin

_password_: kavpaljpg

### AppKav - Alvar Aquitectura Page
Se puede acceder a la pagina de admin mediante la url:
```bash
  localhost:8000/AppKav/
```
La pagina en desarrollo cuenta con botones para poder navegar y realizar las acciones correspondientes para el testeo.
Otra forma de entrar a cada es mediantes los siguientes urls:
_inicio_
```bash
  localhost:8000/AppKav/
```
_registrar usuario_
```bash
  localhost:8000/AppKav/registrar_usuario.html
```
_ver usuarios_
```bash
  localhost:8000/AppKav/ver_usuario.html
```
_crear consulta_
```bash
  localhost:8000/AppKav/crear_consulta.html
```
_ver consultas_
```bash
  localhost:8000/AppKav/ver_consultas.html
```

Estan sin funcionamiento aun las urls correspondientes a la seccion de Proyectos
```bash
  localhost:8000/AppKav/crear_proyecto.html

  localhost:8000/AppKav/ver_proyecto.html 
```
### Observacion - Templates

Los templates aun estan en desarrollo. Se puede ver algo desordenado y sin correspondencia entre diferentas paginas del mismo proyecto. Es todavia una seccion en desarrollo
