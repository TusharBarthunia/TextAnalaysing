# i have created this file -MATT 
from typing import Text
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')         #Getting the text
    #checking checkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    charcount=request.POST.get('charcount','off')
    
    #check which is on
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        dictionary={
            'purpose':'Removed Punctuations',
            'analyzed_text':analyzed
        }
        return render(request,'analyze.html',dictionary)
    elif(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
            dictionary={
            'purpose':'Changed to Uppercase',
            'analyzed_text':analyzed
        }
        return render(request,'analyze.html',dictionary)
    elif(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r" :
                analyzed=analyzed + char
            dictionary={
            'purpose':'Remove NewLines',
            'analyzed_text':analyzed
        }
        return render(request,'analyze.html',dictionary)
    elif(spaceremover=="on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and  djtext[index+1]==" "):
                analyzed=analyzed + char
                
            
            dictionary={
            'purpose':'Remove NewLines',
            'analyzed_text':analyzed
        }
        return render(request,'analyze.html',dictionary)
    elif(charcount=="on"):
        count=0
        for i in djtext:
            count+=1
        
        dictionary={
            'purpose':'Count character',
            'analyzed_text':count
        }
        return render(request,'analyze.html',dictionary)
    else:
       return HttpResponse("Error")