from django.shortcuts import render
from django.conf.urls import handler404, handler500


def hotel_list(request):
    return render(request, "accommodation/hotel_list.html")
