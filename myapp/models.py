from django.db import models
from django.utils import timezone

# Create your models here.

class usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    correo_usuario = models.EmailField()
    contrasena_usuario = models.CharField(max_length=50)
    

class extrausuario(models.Model):
    progreso_curso = models.IntegerField()  
    avatar_usuario = models.CharField(max_length=10000)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    
    
class soportetecnico(models.Model):
    
    categoria_reporte = models.CharField(max_length=50)
    descripcion_reporte = models.CharField(max_length=1000)
    fecha_reporte = models.DateTimeField()
    estado_reporte = models.CharField(max_length=50)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    comentario_soporte = models.CharField(max_length=1000)
    
class control(models.Model):
    tipo_usuario = models.CharField(max_length=50)
    fecha_control = models.DateTimeField(default=timezone.now)
    accion = models.CharField(max_length=50)

    @property
    def antiguedad_usuario(self):
        tiempo_transcurrido = timezone.now() - self.fecha_control
        print(tiempo_transcurrido)
        return tiempo_transcurrido.days