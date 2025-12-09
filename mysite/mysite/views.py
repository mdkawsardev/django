from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello World. Welcome to Home")
    return render(request, 'website/index.html')
def about(request):
    return HttpResponse("Hello World. Welcome to about")
def contact(request):
    return HttpResponse("Hello World. Welcome to contact")
