
from django.db import models
from django.conf import settings
from datetime import datetime
from uuid import uuid4
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location=settings.MEDIA_ROOT)


def user_directory_path(instance, filename):
    ext = filename.split("-")[-1]

    return "{0}.{1}".format(uuid4(), ext)


class Brand(models.Model):
    name = models.CharField(max_length=50, verbose_name="Brand")
    image = models.ImageField(upload_to=user_directory_path, default="")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Showroom(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    brand = models.ManyToManyField(
        Brand,  default="")

    created_at = models.DateTimeField(
        auto_now_add=True)

    def __str__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.PositiveIntegerField()
    showroom = models.ForeignKey(
        Showroom, on_delete=models.CASCADE, null=False, )
    image = models.ImageField(upload_to=user_directory_path,default="")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Joining Date")

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=50, verbose_name="Model")
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, null=False, default="")

    def __str__(self):
        return self.name


class Engine(models.Model):
    name = models.CharField(max_length=50, verbose_name="Engine")
    model = models.OneToOneField(Model, on_delete=models.CASCADE, default="")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=50)
    model = models.ManyToManyField(Model)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=50)

    image = models.ImageField(upload_to=user_directory_path, default="")

    showroom = models.ForeignKey(
        Showroom, on_delete=models.CASCADE, null=False)
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, null=False)
    model = models.ForeignKey(
        Model, on_delete=models.CASCADE, null=False, default="")

    stock = models.PositiveIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
