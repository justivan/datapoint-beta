from django.urls import path
from .views import (
    UserListAPIView,
    CountryListAPIView,
    RegionListAPIView,
    AreaListAPIView,
)

app_name = "api"
urlpatterns = [
    path("user/", UserListAPIView.as_view(), name="user-list"),
    path("country/", CountryListAPIView.as_view(), name="country-list"),
    path("region/", RegionListAPIView.as_view(), name="region-list"),
    path("area/", AreaListAPIView.as_view(), name="area-list"),
]
