from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.contrib.auth.models import User
from app_user.models import *
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login


import sys
import os
import json

# Create your views here.
def login(request):
    response = TemplateResponse(request, 'login.html', {})
    return response

def autenticar(request):
    usuario = request.POST.get('user','')
    clave = request.POST.get('password','')
    try:
        usuarioAuth =  authenticate(email="ca@ca.com", password="ca")
        print usuarioAuth
        if usuarioAuth is not None:                
            auth_login(request, usuarioAuth)
            print "User autenticado"
        else:
            print "fallo"
    except Exception as error:
            print str(error)
            print 'Error on line {}'.format(sys.exc_info()[-1].tb_lineno)
            return HttpResponse(json.dumps({'status':0,'mensaje': "Se presento un error ",'data': [] }),content_type="application/json")     