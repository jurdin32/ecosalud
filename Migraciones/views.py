from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
# Create your views here.
from Prestadores.models import Departamentos, Municipios, SedesPrestador, DetalleSede
from ecosalud.settings import BASE_DIR

#archivo = BASE_DIR/"antioquia.xlsb"
#df = pd.read_excel(archivo, sheet_name='Sedes')

# def lugares(codigo):
#     contador=0
#     creados=0
#     for i in df.values:
#         contador+=1
#         try:
#             if codigo==0:
#                 registro=Departamentos.objects.get(nombre=i[codigo])
#             elif codigo==1:
#                 registro = Municipios.objects.get(nombre=i[codigo],depatamento__nombre=i[0])
#         except:
#             if codigo==0:
#                 dep=Departamentos.objects.create(nombre=i[codigo])
#                 dep.save()
#             elif codigo==1:
#                 dep = Departamentos.objects.get(nombre=i[0])
#                 mun=Municipios.objects.create(nombre=i[codigo], depatamento=dep)
#                 mun.save()
#             creados += 1
#         print("[%s] "%contador,i[codigo])
#     print("Cantidad de registros creados:",creados)
#
# def prestadores():
#     contador=0
#     creados=0
#     for i in df.values:
#         contador+=1
#         try:
#             prest=SedesPrestador.objects.get(nit=i[18])
#         except:
#             mun=Municipios.objects.get(nombre=i[1])
#             prest=SedesPrestador.objects.create(
#                 municipio=mun,nombre_prestador=i[3],nit=i[18],dv=str(i[19]),clase_persona=i[20],naturaleza=i[22],clase_prestador=i[24]
#             )
#             prest.save()
#             creados+=1
#         print("[%s] " % contador, i[3])
#     print("Cantidad de registros creados:", creados)
#
# def detalle_sede():
#     contador = 0
#     creados = 0
#     for i in df.values:
#         contador += 1
#         prest = SedesPrestador.objects.get(nit=i[18])
#         try:
#             det=DetalleSede.objects.get(sede=prest,numero_sede=i[5])
#         except:
#             det=DetalleSede.objects.create(
#                 sede=prest, codigo_habilitacion=i[4],numero_sede=i[5],nombre=i[6],gerente=i[7],
#                 direccion=i[9],telefono=i[13],email=i[15],fecha_apertura=i[16],
#                 horario_lunes=i[31],horario_martes=i[32],horario_miercoles=i[33],horario_jueves=i[34],
#                 horario_viernes=i[35],horario_sabado=i[36],horario_domingo=i[37]
#             )
#             det.save()
#             creados+=1
#         print("[%s] " % contador, i[3])
#     print("Cantidad de registros creados:", creados)
#
# def migracion_det_prestador(request):
#     detalle_sede()
#     return HttpResponse("ok")
#
# def migracion_prestadores(request):
#     prestadores()
#     return HttpResponse("ok")
#
# def migracion_dep(request):
#     lugares(1) #0 para departamentos, 1 para municipios
#     return HttpResponse("ok")