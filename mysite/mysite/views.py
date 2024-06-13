# I have created this file - Maysha Khanom Moon
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removePunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')
    
    print(removePunc)
    print(djtext)
    
    # Analyze the text
    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    analyzed = ""
    purpose = ""
    
    if removePunc != 'off':
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        djtext = analyzed
        analyzed = ""
    
        purpose += 'Removed Puntuations\n'
    
    if fullcaps == 'on':
        for char in djtext:
            analyzed += char.upper()
            
        djtext = analyzed
        analyzed = ""
        purpose += 'Change to Uppercase\n'
    
        # params = {'purpose': 'Change to Uppercase', 'analyzed': analyzed}
        # return render(request, 'analyze.html', params)
    
    if newlineremover == 'on':
        for char in djtext:
            if char is not '\n' and char != '\r':
                analyzed += char
        
        djtext = analyzed
        analyzed = ""
        purpose += 'Romoved New Line'
    
        params = {'purpose': 'Removed New Line', 'analyzed': analyzed}
        # return render(request, 'analyze.html', params)
    
    if extraspaceremover == 'on':
        for index, char in enumerate(djtext):
            if djtext[index] == ' ' and djtext[index+1] == ' ':
                pass
            else:
                analyzed += char

        djtext = analyzed
        analyzed = ""
        purpose += 'Romoved Extra Spaces\n'
        
        # params = {'purpose': 'Removed Extra Spaces', 'analyzed': analyzed}
        # return render(request, 'analyze.html', params)
    
    if charcounter == 'on':
        # analyzed = len(djtext)
        
        if purpose:
            analyzed = djtext + '\n\n'
        
        analyzed += 'Total number of characters: ' + str(len(djtext))
        djtext = analyzed
        purpose += 'Character Counter\n'
    
        # params = {'purpose': 'Character Counter', 'analyzed': analyzed}
        # return render(request, 'analyze.html', params)
    
    if purpose:
        params = {'purpose': purpose, 'analyzed': djtext}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('Please select any operation and try again!')
    