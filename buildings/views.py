from django.shortcuts import render
from django.utils import timezone
from django.views.generic.list import ListView
from buildings.models import Building
from django.contrib import admin
from .models import Ticket, Department, Room
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *


def index(request):
    return render(request, "index.html")


@api_view(["POST"])
def postTicket(request):
    serializer = TicketSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["GET"])
def getTicket(request):
    ticket = Ticket.objects.all()
    serializer = TicketSerializer(ticket, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getDepartment(request):
    department = Department.objects.all()
    serializer = DepartmentSerializer(department, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def getRoom(request):
    room = Room.objects.all()
    serializer = RoomSerializer(room, many=True)
    return Response(serializer.data)


class EventAdminSite(admin.AdminSite):
    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        ordering = {
            "Buildings": 1,
            "Blocks": 2,
            "Floors": 3,
            "Rooms": 4,
            "Items": 5,
        }
        app_dict = self._build_app_dict(request)

        app_list = sorted(app_dict.values(), key=lambda x: x["name"].lower())

        for app in app_list:
            app["models"].sort(key=lambda x: ordering[x["name"]])

        return app_list
