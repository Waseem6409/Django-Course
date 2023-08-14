from django.contrib import admin
from django.utils.html import format_html
from .models import Showroom, Staff, Brand, Car, Model, Feature, Engine

# Register your models here.


@admin.register(Showroom)
class Admin(admin.ModelAdmin):
    list_display = ("name", "created_at", "address",
                    "brands_available",  "models_available", "number_of_staff")

    def brands_available(self, obj):

        return "".join([f"{str(record)}, " for record in obj.brand.all()])

    def models_available(self, obj):
        text = ""
        for brand in obj.brand.all():
            for model in brand.model_set.all():
                text += f"{str(model)}, "
        return text

    def number_of_staff(self, obj):

        return Staff.objects.filter(showroom=obj.id).count()


@admin.register(Staff)
class Admin(admin.ModelAdmin):
    list_display = ("name",  "showroom", "created_at")

    def number_of_staff(self, obj):

        return Staff.objects.filter(showroom=obj.id).count()


@admin.register(Brand)
class Admin(admin.ModelAdmin):
    list_display = ("name", "models", "available_at_showroom")

    def models(self, obj):
        return "".join([f"{str(record)}, " for record in Model.objects.filter(brand=obj.id)])

    def available_at_showroom(self, obj):
        return "".join([f"{str(record)}, " for record in Showroom.objects.filter(brand=obj.id)])


@admin.register(Car)
class Admin(admin.ModelAdmin):
    list_display = ("name", "car_image",  "showroom",
                    "brand", "model", "stock", "created_at")

    def car_image(self, obj):
        return format_html('<img src="{}" width="auto" height="100px" />'.format(obj.image.url))


@admin.register(Model)
class Admin(admin.ModelAdmin):
    list_display = ("name",  "brand", "features")

    def features(self, obj):
        return "".join([f"{str(record)}, " for record in obj.feature_set.all()])


@admin.register(Feature)
class Admin(admin.ModelAdmin):
    list_display = ("name",  "available_in_model")

    def available_in_model(self, obj):

        return "".join([f"{str(record)}-{str(record.brand)}, " for record in obj.model.all()])


@admin.register(Engine)
class Admin(admin.ModelAdmin):
    list_display = ("name",  "model", "brand")

    def brand(self, obj):

        return obj.model.brand
