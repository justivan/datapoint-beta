from django.urls import path
from .views import hotel_list

app_name = "accommodation"
urlpatterns = [
    path("hotel/", hotel_list, name="hotel-list"),
]
