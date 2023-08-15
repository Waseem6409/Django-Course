from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Brand, Car, Engine, Model, Staff

# Create your views here.


def Home(request: HttpRequest):
    brands = Brand.objects.all()
    return render(request, "Home.html", {"brands": brands})


def Team(request: HttpRequest):
    staffs = Staff.objects.all()
    return render(request, "Team.html", {"staffs": staffs})


def BrandDetail(request: HttpRequest, id: int = None):
    brand = Brand.objects.get(id=id)
    cars = Car.objects.filter(brand=id)

    for car in cars:

        engine = Engine.objects.filter(model=car.model.id)
        if (engine.count() > 0):

            car.engine = engine[0]

    return render(request, "BrandDetail.html", {"brand": brand, "cars": cars})
