# I have created this file - Maysha Khanom Moon
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>hello, Maysha Khanom Moon</h1><a href="about">about</a>')

def about(request):
    return HttpResponse('about Maysha Khanom Moon')