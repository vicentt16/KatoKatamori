from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def HomePage(request):
   template = loader.get_template('HomePage.html')
   return HttpResponse(template.render())