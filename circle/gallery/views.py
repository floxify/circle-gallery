# Create your views here.
# _*_ coding:utf-8 _*_

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context,RequestContext

from bcsutil import list_obj_urls

def index(request):
    obj_urls = list_obj_urls()
    variables = RequestContext(request, {
            'obj_urls' : obj_urls
            })
    return render_to_response('index.html',variables)


