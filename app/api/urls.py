from django.urls import path
from .views import user_list, country_list, region_list, area_list, hotel_api_view

app_name = "api"
urlpatterns = [
    path("user/", user_list, name="user-list"),
    path("country/", country_list, name="country-list"),
    path("region/", region_list, name="region-list"),
    path("area/", area_list, name="area-list"),
    path("hotel/", hotel_api_view, name="hotel-list"),
]
