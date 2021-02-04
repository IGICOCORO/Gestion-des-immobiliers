from django.shortcuts import render

def home(request):
    
    return render(request, 'loyer/index.html')