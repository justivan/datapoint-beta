from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.gis.geos import Point
from django.contrib.auth import get_user_model

from definitions.models import Country, Region, Area
from definitions.serializers import CountrySerializer, RegionSerializer, AreaSerializer
from accommodation.models import PurchaseManager, SalesContact, HotelChain, Hotel
from accommodation.serializers import PurchaseManagerSerializer, SalesContactSerializer, HotelSerializer
from users.serializers import UserSerializer

User = get_user_model()


@api_view(["GET", "POST"])
def user_list(request):
    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def country_list(request):
    countries = Country.objects.all()
    serializer = CountrySerializer(countries, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def region_list(request):
    regions = Region.objects.all()
    serializer = RegionSerializer(regions, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def area_list(request):
    lat = request.query_params.get("lat")
    lng = request.query_params.get("lng")

    if lat is not None and lng is not None:
        point = Point(float(lng), float(lat), srid=4326)
        queryset = Area.objects.filter(geom__contains=point)
    else:
        queryset = Area.objects.all()

    serializer = AreaSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def hotel_api_view(request):
    if request.method == "POST":
        queryset = Hotel.objects.select_related(
            "category",
            "area",
            "chain",
            "sales_contact",
            "purchase_manager",
            "status",
        ).prefetch_related("tags")

        # infinite scroll
        start_row = int(request.data.get("startRow", 0))
        end_row = int(request.data.get("endRow", 50))

        queryset = queryset[int(start_row) : int(end_row)]
        serializer = HotelSerializer(queryset, many=True)
        return Response(serializer.data)

    return Response({"error": "Unsupported method"}, status=405)
