from django.contrib import admin
from easy_select2 import select2_modelform
from .models import RoomItem, ActivityItem, Ticket


class RoomItemInline(admin.TabularInline):
    model = RoomItem
    extra = 1


class ActivityItemInline(admin.TabularInline):
    model = ActivityItem
    extra = 1


class MaintenanceTicketInline(admin.StackedInline):
    model = Ticket
    extra = 1
