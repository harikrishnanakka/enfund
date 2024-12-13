from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')

def chat_view(request):
    return render(request,'chat.html')

def landing_view(request):
    return render(request,'landing.html')
