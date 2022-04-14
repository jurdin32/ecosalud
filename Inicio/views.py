# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string

from Prestadores.models import DetalleSede
from ecosalud.envio_email import enviarEmail

def index(request):
    if request.POST:
        if request.GET.get('register'):
            user=User()
            user.email = request.POST.get('email')
            user.username = request.POST.get('email')
            if request.POST.get('nit'):
                user.first_name=request.POST.get('nit')
                user.is_staff=True
            user.is_active=False
            user.set_password(request.POST.get('password1'))
            user.save()
            mensaje = render_to_string('confirmacion.html', {'usuario': str(user.email)})
            enviarEmail(destinatarios=[user.email], asunto="Gracias por tu registro", mensaje=mensaje, is_html=True)
            return HttpResponseRedirect("/success/?user="+user.username)
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect("/myaccount/?iniciarSesion=ok")
    return render(request,'index.html')

def loginView(request):
    if request.POST:
        user = authenticate(username=request.POST.get('user'), password=request.POST.get('passwd'),is_active=True)
        if user:
            login(request,user)
            return HttpResponseRedirect("/myaccount/?iniciarSesion=ok")
        else:
            return HttpResponseRedirect("/")
    else:
        return render(request, 'index.html')

@login_required(login_url='/login')
def logoutView(request):
    logout(request)
    return HttpResponseRedirect('/')

def registro(request):
    usuario=None
    if request.GET.get('user'):
        usuario=User.objects.get(username=request.GET.get('user'))
    elif request.GET.get('renew'):
        usuario = User.objects.get(username=request.GET.get('renew'))
        mensaje=render_to_string('confirmacion.html', {'usuario':str(usuario.email)})
        enviarEmail(destinatarios=[usuario.email],asunto="Gracias por tu registro",mensaje=mensaje,is_html=True)
    elif request.GET.get('activate'):
        usuario = User.objects.get(username=request.GET.get('activate'))
        usuario.is_active=True
        usuario.save()
        return HttpResponse("ok")
    contexto={
        'usuario':usuario
    }
    return render(request,'registro_exitoso.html',contexto)

def forgot_password(request):
    if request.POST:
        print(request.POST)
        try:
            usuario=User.objects.get(email=request.POST.get('email'))
            messages.add_message(request, messages.SUCCESS,"Se ha enviado un email con los pasos a seguir para recuperar la contraseña..!")
            mensaje = render_to_string('forgot.html', {'usuario': str(usuario.email)})
            enviarEmail(destinatarios=[usuario.email], asunto="Gracias por tu registro", mensaje=mensaje, is_html=True)
        except:
            messages.add_message(request,messages.ERROR, "El Email no esta registrado en nuestra base de datos, reintente..!")
    if request.GET.get('user'):
        if request.POST:
            usuario = User.objects.get(username=request.GET.get('user'))
            if request.GET.get('password1') == request.POST.get('password2'):
                usuario.set_password(request.POST.get('password1'))
                usuario.save()
                messages.add_message(request, messages.SUCCESS,"Su contraseña se recuperó con exito..!")
            else:
                messages.add_message(request, messages.ERROR, "Las contraseñas no coinciden, Reintente..!")
        return render(request,'recovery_password.html')

    return render(request,'forgot_password.html',)


@login_required(login_url="/")
def micuenta(request):
    if request.POST:
        print(request.POST)
        user=request.user
        if request.POST.get('password1')==request.POST.get('password2') and request.POST.get('password2') and request.POST.get('password1'):
            user.set_password(request.POST.get('password2'))
        user.email=request.POST.get('email')
        user.username=request.POST.get('email')
        user.save()
        return HttpResponseRedirect("/myaccount/?iniciarSesion=ok")
    if request.GET.get('servicios'):
        try:
            sede=DetalleSede.objects.get(id=request.GET.get('servicios'))
            sede.es_usada=True
            sede.save()
            return HttpResponseRedirect("/myaccount/?sedes=ok")
        except:
            pass
    if request.GET.get('disable'):
        try:
            sede=DetalleSede.objects.get(id=request.GET.get('disable'))
            sede.es_usada=False
            sede.save()
            return HttpResponseRedirect("/myaccount/?sedes=ok")
        except:
            pass
    contexto={
        'ips':DetalleSede.objects.filter(sede__nit=request.user.first_name).order_by('numero_sede')
    }
    return render(request,'micuenta.html',contexto)