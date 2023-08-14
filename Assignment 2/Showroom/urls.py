
from django.urls import path
from .views import Home, Team, BrandDetail

urlpatterns = [
    path("", Home, name="Home"),
    path("team/", Team, name="Team"),
    path("brand-detail/<int:id>", BrandDetail, name="BrandDetail"),
]
