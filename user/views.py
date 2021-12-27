from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'user/login.html')

def home(request):
    return render(request, 'user/home.html')

def receive(request):
    return render(request, 'user/receive.html')