# I have created this file - Maysha Khanom Moon
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name': 'harry', 'place': 'Mars'}
    return render(request, 'index.html', params)

def removePunc(request):
    return HttpResponse('Remove Punctuation')

def capFirst(request):
    return HttpResponse('Capitaliz First')