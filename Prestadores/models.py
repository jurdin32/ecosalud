from django.db import models

# Create your models here.
class Departamentos(models.Model):
    nombre = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural="1. Crear los Departamentos"

    def __str__(self):
        return self.nombre

class Municipios(models.Model):
    depatamento=models.ForeignKey(Departamentos,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=60)

    class Meta:
        verbose_name_plural="1.1. Crear los Municipios"

    def __str__(self):
        return self.nombre

class SedesPrestador(models.Model):
    municipio=models.ForeignKey(Municipios,on_delete=models.CASCADE)
    nombre_prestador=models.TextField(null=True,blank=True)
    nit=models.CharField(max_length=20,null=True,blank=True)
    dv =models.CharField(max_length=5, null=True,blank=True)
    clase_persona=models.CharField(max_length=100,null=True,blank=True)
    naturaleza=models.CharField(max_length=100,null=True,blank=True)
    clase_prestador=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.nombre_prestador

    class Meta:
        verbose_name_plural="2. Crear Prestadores"

class DetalleSede(models.Model):
    sede=models.ForeignKey(SedesPrestador,on_delete=models.CASCADE)
    codigo_habilitacion = models.CharField(max_length=100,null=True,blank=True)
    numero_sede=models.CharField(max_length=2,null=True,blank=True)
    nombre=models.TextField(null=True,blank=True)
    gerente=models.CharField(max_length=60,null=True,blank=True)
    direccion=models.TextField(null=True,blank=True)
    telefono=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=130,null=True,blank=True)
    fecha_apertura=models.CharField(max_length=60,null=True,blank=True)
    horario_lunes=models.CharField(max_length=60,null=True,blank=True)
    horario_martes=models.CharField(max_length=60,null=True,blank=True)
    horario_miercoles=models.CharField(max_length=60,null=True,blank=True)
    horario_jueves=models.CharField(max_length=60,null=True,blank=True)
    horario_viernes=models.CharField(max_length=60,null=True,blank=True)
    horario_sabado=models.CharField(max_length=60,null=True,blank=True)
    horario_domingo=models.CharField(max_length=60,null=True,blank=True)
    es_usada=models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural="2.1. Crear Las Sedes"
