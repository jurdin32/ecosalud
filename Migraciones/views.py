from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import pandas as pd
# Create your views here.
from Prestadores.models import Departamentos, Municipios, SedesPrestador, DetalleSede
from ecosalud.settings import BASE_DIR

def lugares(codigo):
    archivo = BASE_DIR / "antioquia.xlsb"
    df = pd.read_excel(archivo, sheet_name='Sedes')
    contador=0
    creados=0
    for i in df.values:
        contador+=1
        try:
            if codigo==0:
                registro=Departamentos.objects.get(nombre=i[codigo])
            elif codigo==1:
                registro = Municipios.objects.get(nombre=i[codigo],depatamento__nombre=i[0])
        except:
            if codigo==0:
                dep=Departamentos.objects.create(nombre=i[codigo])
                dep.save()
            elif codigo==1:
                dep = Departamentos.objects.get(nombre=i[0])
                mun=Municipios.objects.create(nombre=i[codigo], depatamento=dep)
                mun.save()
            creados += 1
        print("[%s] "%contador,i[codigo])
    print("Cantidad de registros creados:",creados)

def prestadores():
    archivo = BASE_DIR / "antioquia.xlsb"
    df = pd.read_excel(archivo, sheet_name='Sedes')
    contador=0
    creados=0
    for i in df.values:
        contador+=1
        try:
            prest=SedesPrestador.objects.get(nit=i[18])
        except:
            mun=Municipios.objects.get(nombre=i[1])
            prest=SedesPrestador.objects.create(
                municipio=mun,nombre_prestador=i[3],nit=i[18],dv=str(i[19]),clase_persona=i[20],naturaleza=i[22],clase_prestador=i[24]
            )
            prest.save()
            creados+=1
        print("[%s] " % contador, i[3])
    print("Cantidad de registros creados:", creados)

def detalle_sede():
    archivo = BASE_DIR / "antioquia.xlsb"
    df = pd.read_excel(archivo, sheet_name='Sedes')
    contador = 0
    creados = 0
    for i in df.values:
        contador += 1
        prest = SedesPrestador.objects.get(nit=i[18])
        try:
            det=DetalleSede.objects.get(sede=prest,numero_sede=i[5])
        except:
            det=DetalleSede.objects.create(
                sede=prest, codigo_habilitacion=i[4],numero_sede=i[5],
                nombre=i[6],gerente=i[7],
                direccion=i[9],telefono=i[13],email=i[15],fecha_apertura=i[16],
                horario_lunes=i[31],horario_martes=i[32],horario_miercoles=i[33],horario_jueves=i[34],
                horario_viernes=i[35],horario_sabado=i[36],horario_domingo=i[37]
            )
            det.save()
            creados+=1
        print("[%s] " % contador, i[3])
    print("Cantidad de registros creados:", creados)

def migracion_det_prestador(request):
    detalle_sede()
    return HttpResponseRedirect("/migracion/")

def migracion_prestadores(request):
    prestadores()
    return HttpResponseRedirect("/migracion/")

def migracion_dep(request,codigo):
    lugares(codigo) #0 para departamentos, 1 para municipios
    return HttpResponseRedirect("/migracion/")

def corregirdv(request):
    for i in SedesPrestador.objects.all():
        if i.dv=='nan':
            i.dv=""
            i.save()
        elif i.dv=='':
            pass
        else:
            digito = float(i.dv)
            i.dv=(int(digito))
            i.save()
    return HttpResponseRedirect("/migracion/")

def corregirgerente(request):
    for i in DetalleSede.objects.all():
        if i.gerente=='nan':
            i.gerente=""
            i.save()
        if i.horario_lunes=='nan':
            i.horario_lunes=""
            i.save()
        if i.horario_martes=='nan':
            i.horario_martes=""
            i.save()
        if i.horario_miercoles=='nan':
            i.horario_miercoles=""
            i.save()
        if i.horario_jueves=='nan':
            i.horario_jueves=""
            i.save()
        if i.horario_viernes=='nan':
            i.horario_viernes=""
            i.save()
        if i.horario_sabado=='nan':
            i.horario_sabado=""
            i.save()
        if i.horario_domingo=='nan':
            i.horario_domingo=""
            i.save()
    return HttpResponseRedirect("/migracion/")


def migracion(request):
    return render(request,'migracion.html')