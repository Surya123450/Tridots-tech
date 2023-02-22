from django.shortcuts import render


# Create your views here.

def display(request):
    return render(request,'LMSapp\\index.html')

def check(request):
    return render(request,'LMSapp\\chapter1.html')