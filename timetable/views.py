from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

def index(request):
    return HttpResponse("Under construction!")

def redirect_to_index(request):
    return redirect(reverse('index'))