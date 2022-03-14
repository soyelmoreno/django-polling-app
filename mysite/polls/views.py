# from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def wow(request):
    return HttpResponse("Wow, it works. You're at the polls Wow page.")
