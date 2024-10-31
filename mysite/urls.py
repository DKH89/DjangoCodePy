"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('Noticias/',views.noticias),
    path('Recursos/',views.recursos),
    path('ChatBot/',views.chatBot),
    path('Soporte/',views.soporte),
    path('Nosotros/',views.nosotros),
    path('CursoPython/',views.cursoPython),
    
    path('Login/',views.IniciarSesion),
    path('Registro/',views.RegistrarUsuario),
        
    path('sintaxisEntrada/',views.sintaxisEntrada),
    path('sintaxisVariables/',views.sintaxisVariables),
    path('sintaxisComentarios/',views.sintaxisComentarios),
    
    path('EstructurasCondicionales/',views.EstructurasCondicionales),
    path('EstructurasCiclicas/',views.EstructurasCiclicas),
    path('EstructurasListas/',views.EstructurasListas),
    path('EstructuraTuplas/',views.EstructurasTuplas),
    path('EstructuraDiccionarios/',views.EstructurasDiccionarios),
    

    path('FuncionesDefinicion/',views.FuncionesDefinicion),
    path('FuncionesRecursividad/',views.FuncionesRecursividad),
    path('FuncioneTipos/',views.FuncionesTipos),
    path('FuncioneArgumentos/',views.FuncionesArgumentos),

    
    path('Poo-Clases/',views.POO_Clases),
    path('Poo-Herencia/',views.POO_Herencia),
    path('Poo-Encapsulamiento/',views.POO_Encapsulamiento),
    path('Poo-Polimorfismo/',views.POO_Polimorfismo),
    
    
    
    path('EliminaSoporte/',views.eliminarTodosSoportes),
    path('OperadoresAsignacion/',views.OperadoresAsignacion),
    path('OperadoresAritmeticos/',views.OperadoresAritmeticos),
    path('OperadoresRelacionales/',views.OperadoresRelacionales),
    path('OperadoresLogicos/',views.OperadoresLogicos),
    
    
    
    path('Evaluacion1/',views.Evaluacion1),
    path('Evaluacion2/',views.Evaluacion2),


    path('actualizarNota1/<nota>',views.actualizarNota1),
    path('actualizarNota2/<nota>',views.actualizarNota2),

    
    path('Avatar/',views.Avatar),
    path('Perfil/',views.Perfil),
    path('PerfilAdmin/',views.PerfilAdmin),

    path('AvatarLog/',views.AvatarLog),
    
    path('Perfil/Soporte',views.SoportePerfil),


    path('PerfilActualizarNombre/<nombre>',views.actualizarNombreusuario),
    
    path('PerfilActualizarCorreo/<correo>',views.actualizarCorreousuario),

    path('PerfilActualizarContrasena/<contrasena>',views.actualizarContrasenausuario),

    path('PerfilEliminarUsuario/<id>',views.eliminarUsuario),

    path('RegistrarUsuario/<nombre>/<correo>/<contrasena>',views.crearUsuario),

    path('IniciarSesion/<correo>/<contrasena>',views.VerificarUsuario),
    
    path('EnviarSoporte/<categoria>/<descripcion>/<fecha>/<estado>/<usuario_id>/<comentario>',views.crearsoportecnico),


    path('RegistrarPerfil/<usuario_id>/<avatar>' , views.crearInfoUsuario),
    
    path('ActualizarAvatar/<avatar>' , views.actualizarAvatar),

    path('InteligenciaArtificial/',views.inteligenciaArtificial),

    path('InteligenciaArtificialCompleto/',views.interfazIA),
    
    path('Perfil/Progreso',views.progreso),
    
    path('Desloguearse/',views.desloguearse),


    path('DescargarDiploma/',views.generar_diploma),


    path('CargarUsuario/<id_usuario>',views.cargarusuariporid),

    
    path('ActualizarDatosUsuario/<id_usuario>/<nombre>/<correo>/<contrasena>',views.actualizardatosusuario),
    
    path('SoporteAdmin/',views.SoporteAdmin),

    path('ActualizarEstadoReporte/<id_reporte>/<estado_reporte>/<comentario_reporte>',views.actualizarestadoreporte),

]
