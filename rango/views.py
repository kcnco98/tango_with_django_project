from django.shortcuts import render


from django.http import HttpResponse

def index(request):
    href = '<a href="/rango/about/">About</a>'
    return HttpResponse("Rango says hey there partner!"+href)
    

def about(request):
    href = '<a href="/rango/">Index</a>'
    return HttpResponse("Rango says here is the about page."+href)    
