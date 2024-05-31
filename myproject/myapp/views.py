from django.shortcuts import render, redirect
import csv
from .forms import UploadFileForm
from .models import Location

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

def handle_uploaded_file(file):
    reader = csv.DictReader(file)
    for row in reader:
        Location.objects.create(
            longitude=row['longitude'],
            latitude=row['latitude']
        )

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'].read().decode('utf-8').splitlines())
            return redirect('success')
    else:
        form = UploadFileForm()
    return render(request, 'csvupload/upload.html', {'form': form})

def success(request):
    return render(request, 'csvupload/success.html')