from django.shortcuts import render
from django.http import HttpResponse

def homeRequest(request):
    return render(request, 'index.html')
