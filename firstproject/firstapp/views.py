from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    s='<h1>Hello, Thise basic Project succesfully create by ""AMOL S WALUNJ""</h1>'
    return HttpResponse(s)
