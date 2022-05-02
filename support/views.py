from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Created by : LJH")

# Create your views here.
