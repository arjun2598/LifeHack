from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def amk(request):
    return render(request, 'amk.html')

def bedok(request):
    return render(request, 'bedok.html')

def central(request):
    return render(request, 'central.html')

def jurong(request):
    return render(request, 'jurong.html')

def tanglin(request):
    return render(request, 'tanglin.html')

def woodlands(request):
    return render(request, 'woodlands.html')

def airport(request):
    return render(request, 'airport.html')
