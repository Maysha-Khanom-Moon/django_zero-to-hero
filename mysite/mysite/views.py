# I have created this file - Maysha Khanom Moon
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.GET.get('text', 'default')
    removePunc = request.GET.get('removepunc', 'off')
    print(removePunc)
    print(djtext)
    
    # Analyze the text
    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    analyzed = ""
    
    if removePunc != 'off':
        for char in djtext:
            if char not in punctuations:
                analyzed += char
    
        params = {'purpose': 'Removed Puntuations', 'analyzed': analyzed}
        
        return render(request, 'analyze.html', params)
    
    else:
        return HttpResponse('Error')