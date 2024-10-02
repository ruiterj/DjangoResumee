from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def templates(request):
    return render(request, 'templates.html')

def builder(request):
    return render(request, 'builder.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def account(request):
    return render(request, 'account.html')