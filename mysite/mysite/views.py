# I have created this file - Maysha Khanom Moon
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.GET.get('text', 'default')
    removePunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcounter = request.GET.get('charcounter', 'off')
    
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
    
    elif fullcaps == 'on':
        for char in djtext:
            analyzed += char.upper()
    
        params = {'purpose': 'Change to Uppercase', 'analyzed': analyzed}
        return render(request, 'analyze.html', params)
    
    elif newlineremover == 'on':
        for char in djtext:
            if char is not '\n':
                analyzed += char
    
        params = {'purpose': 'Removed New Line', 'analyzed': analyzed}
        return render(request, 'analyze.html', params)
    
    elif extraspaceremover == 'on':
        for index, char in enumerate(djtext):
            if djtext[index] == ' ' and djtext[index+1] == ' ':
                pass
            else:
                analyzed += char
    
        params = {'purpose': 'Removed Extra Spaces', 'analyzed': analyzed}
        return render(request, 'analyze.html', params)
    
    elif charcounter == 'on':
        analyzed = len(djtext)
        analyzed = 'Total number of characters: ' + str(analyzed)
    
        params = {'purpose': 'Character Counter', 'analyzed': analyzed}
        return render(request, 'analyze.html', params)
    
    else:
        return HttpResponse('Error')