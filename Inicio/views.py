# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string

from ecosalud.envio_email import enviarEmail

def index(request):
    if request.POST:
        if request.GET.get('register'):
            user=User()
            user.email = request.POST.get('email')
            user.username = request.POST.get('email')
            if request.POST.get('nit'):
                user.first_name=request.POST.get('nit')
            user.is_active=False
            user.set_password(request.POST.get('password1'))
            user.save()
            mensaje = render_to_string('confirmacion.html', {'usuario': str(user.email)})
            enviarEmail(destinatarios=[user.email], asunto="Gracias por tu registro", mensaje=mensaje, is_html=True)
            return HttpResponseRedirect("/success/?user="+user.username)
    if request.user.is_authenticated:
        return HttpResponseRedirect("/myaccount/")
    return render(request,'index.html')

def loginView(request):
    if request.POST:
        user = authenticate(username=request.POST.get('user'), password=request.POST.get('passwd'),is_active=True)
        if user:
            login(request,user)
            return HttpResponseRedirect("/")
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


def micuenta(request):
    contexto={

    }
    return render(request,'micuenta.html',contexto)