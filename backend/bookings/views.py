from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Booking

@api_view(["GET"])
def health(request):
    return Response({"status": "ok"})

@api_view(["POST"])
def create_booking(request):
    name = request.data.get("name")
    email = request.data.get("email")
    bookings = Booking.objects.create(name = name,email = email)

    return Response({
        "id": bookings.id,
        "name": bookings.name,
        "email": bookings.email,
    })
