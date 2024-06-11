# I have created this file - Maysha Khanom Moon
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def removePunc(request):
    # default --> when we go through via direct url not from home
    # when there is no GET request --> default
    djtext = request.GET.get('text', 'default')
    print(djtext)
    return HttpResponse('Remove Punctuation')

def capFirst(request):
    return HttpResponse('Capitaliz First')