from django.shortcuts import (render, HttpResponse,)
from django.http.request import HttpRequest


# Create your views here.

def index(request: HttpRequest):
    ctx_title = {'title' : 'Main Page'}
    return render(request, 
        template_name='main/index.html', context=ctx_title)