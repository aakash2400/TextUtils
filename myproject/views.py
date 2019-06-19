from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
    #return HttpResponse("<h1>Welcome To Aakash Dhanwani Project</h1>")    
def removepun(request):
    #print(request.GET.get('text','default'))  aise bi likh skte hai ydi kisi variable mai nhi daale pure print ko to(for get the text )
    djtext=request.GET.get('text','default')
    print(djtext)
    return HttpResponse("Remove punc") 
def result(request):
    #print(request.GET.get('text','default'))  aise bi likh skte hai ydi kisi variable mai nhi daale pure print ko to(for get the text )
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepu','default')
    fullcaps=request.POST.get('fullcaps','default')
    newlineremover=request.POST.get('newlineremover','default')
    extraspaceremover=request.POST.get('extraspaceremover','default')
    charcount=request.POST.get('charcount','default')
    #analyzed=djtext
    if removepunc=="on":
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove Punctuations','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'result.html',params)
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()    
        params={'purpose':'Changed to uppercase','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'result.html',params)
    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char    
        params={'purpose':'Remove new line','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'result.html',params)
    if(extraspaceremover=="on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):    
                analyzed=analyzed+char    
        params={'purpose':'Remove new line','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'result.html',params) 
    if(charcount=="on"):
        analyzed=""
        for char in djtext:
            analyzed=len(djtext)   
        params={'purpose':'For charcount','analyzed_text':analyzed}
    if(removepunc!="on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and charcount!="on"):
        return render(request,'error.html')
    return render(request,'result.html',params) 