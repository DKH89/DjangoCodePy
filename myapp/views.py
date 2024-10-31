from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseServerError
import openai
from django.http import JsonResponse
from myapp.models import usuario , extrausuario
from django.shortcuts import render
from .models import soportetecnico
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from io import BytesIO
from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas


chat_history = []
openai.api_key = "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"

usuarios = {}
infousuarios= {}
soportes = {}
usuariosall = {}
usuariosbuscar = {}
soportesall= {}

def index(request) :
    return render(request, 'index.html' , {'usuario': usuarios})

def noticias(request) :
    return render(request, 'noticias.html',{'usuario': usuarios})

def recursos(request) :
    return render(request, 'recursos.html',{'usuario': usuarios})

def chatBot(request) :
    return render(request, 'chatbot.html',{'usuario': usuarios})

def soporte(request) : 
    return render(request, 'soporte.html',{'usuario': usuarios})
    
def nosotros(request) :
    return render(request, 'nosotros.html',{'usuario': usuarios})

def cursoPython(request) :
    return render(request,'cursopython.html',{'usuario': usuarios})

def interfazIA(request) :
    return render(request,'interfazia.html',{'usuario': usuarios})


def IniciarSesion(request) :
    return render(request,'login.html' , {'usuario': usuarios})

def RegistrarUsuario(request) :
    return render(request,'registro.html',{'usuario': usuarios})


def sintaxisEntrada(request) :
        
    return render(request,'Sintaxis/SintaxisEntrada.html')

def sintaxisVariables(request) :
        
    return render(request,'Sintaxis/sintaxisBasicaVariables.html')

def sintaxisComentarios(request) :
        
    return render(request,'Sintaxis/sintaxisBasicaComentarios.html')



def EstructurasCondicionales(request) :
        
    return render(request,'Estructuras/EstructurasCondicionales.html')

def EstructurasCiclicas(request) :
        
    return render(request,'Estructuras/EstructurasCiclicas.html')

def EstructurasListas(request) :

    return render(request,'Estructuras/EstructurasListas.html')


def EstructurasTuplas(request) :
    
        return render(request,'Estructuras/EstructurasTuplas.html')

def EstructurasDiccionarios(request) :
    
        return render(request,'Estructuras/EstructurasDiccionarios.html')


def FuncionesDefinicion(request) :
    
        return render(request,'Funciones/FuncionesDefinicion.html')

def FuncionesRecursividad(request) :
    
        return render(request,'Funciones/FuncionesRecursividad.html')


def FuncionesTipos(request) :
    
        return render(request,'Funciones/FuncionesTipos.html')
    
def FuncionesArgumentos(request) :
    
        return render(request,'Funciones/FuncionesArgumentos.html')
    
    
def POO_Clases(request) :
    
    return render(request,'POO/POO_clases.html')

    
def POO_Herencia(request) :
    
    return render(request,'POO/POO_Herencia.html')

def POO_Encapsulamiento(request) :
    
    return render(request,'POO/POO_Encapsulamiento.html')

def POO_Polimorfismo(request) :
    
    return render(request,'POO/POO_Polimorfismo.html')


def OperadoresAsignacion(request) :
    
    return render(request,'Operadores/OperadoresAsignacion.html')

def OperadoresAritmeticos(request) :
    
    return render(request,'Operadores/OperadoresAritmeticos.html')

def OperadoresRelacionales(request) :
    
    return render(request,'Operadores/OperadoresRelacionales.html')

def OperadoresLogicos(request) :
        
    return render(request,'Operadores/OperadoresLogicos.html')


def Evaluacion1(request) :
    return render(request,'Evaluaciones/evaluacion1.html',{'usuario': usuarios,'infousuario': infousuarios})

def Evaluacion2(request) :
    return render(request,'Evaluaciones/evaluacion2.html',{'usuario': usuarios,'infousuario': infousuarios})



def Avatar(request) :
    global usuarios
    return render(request,'Perfil/avatar.html', {'usuario': usuarios})


def AvatarLog(request) :
    global usuarios
    return render(request,'Perfil/avatarlog.html', {'usuario': usuarios,'infousuario': infousuarios})

def Perfil(request) :
    global usuarios
    obtenerInfoUsuario()
    global infousuarios
    print(infousuarios)
    return render(request, 'Perfil/perfil.html', {'usuario': usuarios, 'infousuario': infousuarios})


def PerfilAdmin(request) :
    
    global usuarios
    
    global usuariosall
    
    global usuariosbuscar
    
    usuariosall = obtenerusuarios()
    
    return render(request, 'Perfil/perfilAdmin.html', {'usuario': usuarios , 'usuariosall': usuariosall , 'usuariosbuscar': usuariosbuscar})


def SoporteAdmin(request) :
    
    global usuarios
    
    global soportesall
    
    soportesall = obtenersoportes()
         
    return render(request, 'Perfil/soporteadmin.html', {'usuario': usuarios , 'soportes': soportesall})


def progreso(request) :
    global usuarios
    obtenerInfoUsuario()
    global infousuarios
    print(infousuarios)
    return render(request, 'Perfil/progreso.html', {'usuario': usuarios, 'infousuario': infousuarios})



def SoportePerfil(request):
    global usuarios
    print(usuarios)
    
    obtenerInfoUsuario()
    
    global infousuarios
    
    print("Soporte")
    print(infousuarios)
    
    global soportes
    
    try:
        if not usuarios or 'id_usuario' not in usuarios:
            return render(request, 'Perfil/soporteP.html', {'error': 'No existe un perfil para este usuario'})

        if soportes == {}:
            soportes = soportetecnico.objects.filter(usuario_id=usuarios['id_usuario'])
        
        return render(request, 'Perfil/soporteP.html', {'usuario': usuarios, 'infousuario': infousuarios, 'soportes': soportes})

    except soportetecnico.DoesNotExist:
        return render(request, 'login.html', {'error': 'El usuario no tiene soportes técnicos'})
    except Exception as e:
        return render(request, 'login.html', {'error': f'Ha ocurrido un error: {str(e)}'})




# Operaciones Base de datos.
def crearUsuario(request, nombre, correo, contrasena):
    if usuario.objects.filter(correo_usuario=correo).exists():
        
        mensajeRegistro = 'Ya existe un usuario con este correo electrónico'
        return render(request, 'registro.html', {'mensaje': mensajeRegistro})

    else:
        p = usuario(nombre_usuario=nombre, correo_usuario=correo, contrasena_usuario=contrasena)
        p.save()
        mensajeRegistro = 'Usuario creado exitosamente'
        return render(request, 'login.html', {'mensaje': mensajeRegistro})

def VerificarUsuario(request, correo, contrasena):
    try:
        
        p = usuario.objects.get(correo_usuario=correo, contrasena_usuario=contrasena)
        
        global usuarios
        
        usuarios = {"id_usuario":p.id, "nombre_usuario": p.nombre_usuario, "correo_usuario": p.correo_usuario, "contrasena_usuario": p.contrasena_usuario}
       
        print(usuarios)
        
        if usuarios.get("correo_usuario") == "admin@gmail.com":
            return render(request, 'Perfil/perfilAdmin.html', {'usuario': usuarios})
        else:
            try:
                d = extrausuario.objects.get(usuario_id=p.id)
                return render(request, 'Perfil/perfil.html', {'usuario': usuarios})
            except extrausuario.DoesNotExist:
                return render(request, 'Perfil/avatar.html', {'usuario': usuarios})
                
    except usuario.DoesNotExist:
        mensaje = 'Credenciales incorrectas o el usuario no existe'
        return render(request, 'login.html', {'mensaje': mensaje})


def crearInfoUsuario(request ,usuario_id,avatar) :
    
    progreso_curso = 0
    
    p = extrausuario(progreso_curso=progreso_curso,usuario_id=usuario_id,avatar_usuario= avatar)
    
    global usuarios
    
    global infousuarios
    
    infousuarios = {"progreso_curso":p.progreso_curso, "usuario_id":p.usuario_id, "avatar_usuario":p.avatar_usuario}
    
    print(infousuarios)
    
    p.save()
    
    return render(request, 'Perfil/perfil.html', {'usuario': usuarios, 'infousuario': infousuarios})



def actualizarAvatar(request, avatar):
        
        global usuarios
        
        p = extrausuario.objects.get(usuario_id=usuarios['id_usuario'])
        
        p.avatar_usuario = avatar
        
        p.save()
        
        infousuarios = {"progreso_curso":p.progreso_curso, "usuario_id":p.usuario_id, "avatar_usuario":p.avatar_usuario}
        
        return render(request, 'Perfil/perfil.html', {'usuario': usuarios, 'infousuario': infousuarios})



def obtenerInfoUsuario():
    try:
        global usuarios
        
        if not usuarios:
            return "No existe un perfil para este usuario"
        
        d = extrausuario.objects.get(usuario_id=usuarios['id_usuario'])
        
        global infousuarios
        infousuarios = {"progreso_curso": d.progreso_curso, "usuario_id": d.usuario_id, "avatar_usuario": d.avatar_usuario}
    
    except extrausuario.DoesNotExist:
        return "El usuario no existe"
    except Exception as e:
        return f"Ha ocurrido un error: {str(e)}"



def actualizarNombreusuario(request, nombre):
    
    global usuarios
    
    p = usuario.objects.get(id=usuarios['id_usuario'])
    
    p.nombre_usuario = nombre
    
    p.save()
    
    usuarios = {"id_usuario":p.id, "nombre_usuario": p.nombre_usuario, "correo_usuario": p.correo_usuario, "contrasena_usuario": p.contrasena_usuario}
    
    return render(request, 'Perfil/perfil.html', {'usuario': usuarios, 'infousuario': infousuarios})

def actualizarCorreousuario(request, correo):
    
    global usuarios
    
    p = usuario.objects.get(id=usuarios['id_usuario'])
    
    p.correo_usuario = correo
    
    p.save()
    
    usuarios = {"id_usuario":p.id, "nombre_usuario": p.nombre_usuario, "correo_usuario": p.correo_usuario, "contrasena_usuario": p.contrasena_usuario}
    
    return render(request, 'Perfil/perfil.html', {'usuario': usuarios, 'infousuario': infousuarios})

def actualizarContrasenausuario(request, contrasena):
    
    global usuarios
    
    p = usuario.objects.get(id=usuarios['id_usuario'])
    
    p.contrasena_usuario = contrasena
    
    p.save()
    
    usuarios = {"id_usuario":p.id, "nombre_usuario": p.nombre_usuario, "correo_usuario": p.correo_usuario, "contrasena_usuario": p.contrasena_usuario}
    
    return render(request, 'Perfil/perfil.html', {'usuario': usuarios, 'infousuario': infousuarios})


def eliminarUsuario(request, id) :
    
    global usuarios
    
    p = usuario.objects.get(correo_usuario=usuarios['correo_usuario'])
    
    p.delete()
    
    usuarios = {}
    
    return render(request, 'Perfil/perfil.html')



def inteligenciaArtificial(request):
    try:
        if request.method == 'POST':
            user_input = request.POST.get('user_input', '')

            if user_input.lower() == "exit":
                return JsonResponse({"response": "Goodbye!"})
            else:
                chat_history.append({"role": "user", "content": user_input})
                response_iterator = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=chat_history,
                    stream=True,
                    max_tokens=150,
                )

                collected_messages = []

                for chunk in response_iterator:
                    chunk_message = chunk['choices'][0]['delta']
                    collected_messages.append(chunk_message)

                full_reply_content = ''.join([m.get('content', '') for m in collected_messages])
                chat_history.append({"role": "assistant", "content": full_reply_content})
                return JsonResponse({"response": full_reply_content})

        return HttpResponseNotAllowed(['POST'])
    except Exception as e:
        print(f"Error en inteligenciaArtificial: {e}")
        return HttpResponseServerError("Ocurrió un error en el servidor.")

def crearsoportecnico(request, categoria, descripcion, fecha, estado, usuario_id, comentario):
    # Crear y guardar el nuevo reporte de soporte técnico
    p = soportetecnico(
        categoria_reporte=categoria,
        descripcion_reporte=descripcion,
        fecha_reporte=fecha,
        estado_reporte=estado,
        usuario_id=usuario_id,
        comentario_soporte=comentario
    )
    p.save()
    
    # Obtener la información del usuario y sus soportes
    return obtenersoporteusuario(request)



def generar_diploma(request):
    # Configurar el tamaño de la página y el lienzo
    width, height = landscape(letter)
    buffer = BytesIO()

    global usuarios
    nombreusuario = usuarios.get('nombre_usuario')

    # Crear el lienzo PDF
    c = canvas.Canvas(buffer, pagesize=landscape(letter))

    # Definir el color azul claro
    blue_light = colors.HexColor('#ADD8E6') 

    # Dibujar el rectángulo de fondo con el color azul claro
    c.setFillColor(blue_light)
    c.rect(0, 0, width, height, fill=True, stroke=False)

    # Título principal
    c.setFont("Helvetica-Bold", 40)
    c.setFillColorRGB(0, 0, 0)  
    c.drawCentredString(width / 2.0, height - 1.5*inch, "Certificado Curso Python")
    
    logo_path = "myapp/static/imagenes/CodePyAIN.png"
    logo_width = 3 * inch  
    logo_height = 2 * inch  
    logo_x = (width - logo_width) / 2
    logo_y = height - 2.7*inch - (logo_height / 2)
    c.drawImage(logo_path, logo_x, logo_y, width=logo_width, height=logo_height, mask='auto')

    # Texto que presenta el certificado
    c.setFont("Helvetica", 20)
    c.drawCentredString(width / 2.0, height - 4*inch, "Este certificado se otorga a:")

    # Nombre del receptor del certificado
    c.setFont("Helvetica-Oblique", 30)
    c.drawCentredString(width / 2.0, height - 5*inch, nombreusuario)

    # Texto de relleno (Lorem Ipsum)
    c.setFont("Helvetica", 12)
    c.drawCentredString(width / 2.0, height - 6*inch, "Por haber cumplido cabalmente con ")
    c.drawCentredString(width / 2.0, height - 6.5*inch, "todos los requisitos técnicos y de programación")
    c.drawCentredString(width / 2.0, height - 7*inch, "establecidos en nuestro curso")

    # Firmas
    c.setFont("Helvetica", 10)
    c.drawString(1.5*inch, 1.5*inch, "Camilo Ortiz")
    c.drawString(1.5*inch, 1.2*inch, "Fundador CodePyAI")
    c.line(1.5*inch, 1.7*inch, 3.5*inch, 1.7*inch)

    c.drawString(width - 3.5*inch, 1.5*inch, "Cristian Rozo")
    c.drawString(width - 3.5*inch, 1.2*inch, "Fundador CodePyAi")
    c.line(width - 3.5*inch, 1.7*inch, width - 1.5*inch, 1.7*inch)

    # Agregar imágenes de firmas
    c.drawImage("myapp/static/imagenes/Firma2.png", 1.5*inch, 1.8*inch, width=2*inch, height=1*inch, mask='auto')
    c.drawImage("myapp/static/imagenes/Firma3.png", width - 3.5*inch, 1.8*inch, width=2*inch, height=1*inch, mask='auto')

    # Guardar el PDF
    c.save()

    # Enviar el PDF como una descarga directa en la página web
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="diploma.pdf"'
    buffer.seek(0)
    response.write(buffer.read())

    return response

def desloguearse(request):
    
    global usuarios
    global infousuarios
    global soportes
    
    usuarios = {}
    infousuarios = {}
    soportes = {}
    
    return render(request, 'index.html', {'usuario': usuarios})


def obtenersoporteusuario(request):
    global usuarios
    global infousuarios
    global soportes
    
    soportes = soportetecnico.objects.filter(usuario_id=usuarios['id_usuario'])
    
    print("Hola")
    
    print("Hola:",soportes)
    return render(request, 'Perfil/soporteP.html', {'usuario': usuarios, 'infousuario': infousuarios, 'soportes': soportes})


def obtenerusuarios():
    
    usuariosAll = usuario.objects.all()
    return usuariosAll



def obtenersoportes():
    
    soportesAll = soportetecnico.objects.all()
    return soportesAll



def cargarusuariporid(request, id_usuario):
    
    p = usuario.objects.get(id=id_usuario)
    
    global usuarios
    
    global usuariosbuscar
    
    global usuariosall
    
    usuariosbuscar = {"id_usuario":p.id, "nombre_usuario": p.nombre_usuario, "correo_usuario": p.correo_usuario, "contrasena_usuario": p.contrasena_usuario}
    
    print("Hola")
    print(usuariosbuscar)
    
    
    return render(request, 'Perfil/perfilAdmin.html', {'usuario': usuarios , 'usuariosall': usuariosall, 'usuariosbuscar': usuariosbuscar})


def actualizarestadoreporte(request,id_reporte,estado_reporte,comentario_reporte):

    s = soportetecnico.objects.get(id=id_reporte)
    s.estado_reporte = estado_reporte
    s.comentario_soporte = comentario_reporte
    
    
    global usuarios
    
    s.save()
    
    return render(request, 'Perfil/soporteadmin.html' , {'usuario': usuarios})




def actualizardatosusuario(request, id_usuario, nombre, correo, contrasena):
    
    p = usuario.objects.get(id=id_usuario)
    
    p.nombre_usuario = nombre
    p.correo_usuario = correo
    p.contrasena_usuario = contrasena
    
    p.save()
    
    global usuarios
        
    global usuariosall
    
    global usuariosbuscar
    
    usuariosbuscar = {"id_usuario":p.id, "nombre_usuario": p.nombre_usuario, "correo_usuario": p.correo_usuario, "contrasena_usuario": p.contrasena_usuario}
    
    print("hola")
        
    return render(request, 'Perfil/perfilAdmin.html', {'usuario': usuarios , 'usuariosall': usuariosall, 'usuariosbuscar': usuariosbuscar})


    
def actualizarNota1(request , nota):
    
    global usuarios
    
    print(usuarios)

    p = extrausuario.objects.get(usuario_id=usuarios['id_usuario'])
    
    valor = float(nota) * 0.5
    
    p.progreso_curso = valor
    
    global infousuarios
    
    infousuarios = {"progreso_curso":p.progreso_curso, "usuario_id":p.usuario_id, "avatar_usuario":p.avatar_usuario}
    
    p.save()
    
    return render(request,'Evaluaciones/evaluacion1.html',{'usuario': usuarios,'infousuario': infousuarios})

    
def actualizarNota2(request , nota):
    
    global usuarios
    
    print(usuarios)

    p = extrausuario.objects.get(usuario_id=usuarios['id_usuario'])
    
    valor = float(nota) * 0.5
    
    valorTotal = valor + p.progreso_curso
    
    p.progreso_curso = valorTotal
    
    global infousuarios
    
    infousuarios = {"progreso_curso":p.progreso_curso, "usuario_id":p.usuario_id, "avatar_usuario":p.avatar_usuario}
    
    p.save()
    
    return render(request,'Evaluaciones/evaluacion2.html',{'usuario': usuarios,'infousuario': infousuarios})
    
    
    
def eliminarTodosSoportes(request):
        
        soportesAll = soportetecnico.objects.all()
        
        for s in soportesAll:
            s.delete()
        
        return render(request, 'Perfil/soporteadmin.html' , {'usuario': usuarios})