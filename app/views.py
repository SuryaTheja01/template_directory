from django.shortcuts import render

# Create your views here.

def sample(request):
    return render(request,'sample.html')

def h2(request):
    return render(request,'h2.html')
