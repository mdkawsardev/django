from django.shortcuts import render

def new(request):
    return render(request, 'myapp/new.html')
def privacy(request):
    return render(request, 'myapp/privacy.html')
def contact(request):
    return render(request, 'myapp/contact.html')