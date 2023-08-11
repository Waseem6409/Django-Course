from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.


def Index(request: HttpRequest):
    return render(request, 'Index.html')


def Detail(request: HttpRequest):
    return render(request, 'Detail.html')
