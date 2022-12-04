from django.contrib import admin
from easy_select2 import select2_modelform

# Register your models here.
from .models import (
    Building,
    Block,
    Floor,
    Room,
    Item,
    RoomItem,
    Department,
    Maintenance,
    Ticket,
    Activity,
    ActivityItem,
)
from django.contrib import admin


ticket_form = select2_modelform(Ticket, attrs={"width": "250px"})


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ("name", "state", "country")
    list_filter = ("state", "country")
    search_fields = ("name", "state", "country")


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ("name", "floors")
    list_filter = ("name", "floors")
    search_fields = ("name", "floors")


@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display = ("name", "no_rooms")
    list_filter = ("name", "no_rooms")
    search_fields = ("name", "no_rooms")
    raw_id_fields = ("block",)


# @admin.register(RoomItem)
class RoomItemInline(admin.TabularInline):
    model = RoomItem
    extra = 1


class ActivityItemInline(admin.TabularInline):
    model = ActivityItem
    extra = 1


@admin.register(Room)
class roomsAdmin(admin.ModelAdmin):
    list_display = ("room_no", "room_type")
    list_filter = ("room_type", "room_no")
    raw_id_fields = ("floor",)
    search_fields = ("room_no", "room_type")
    inlines = [RoomItemInline]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Item)
class itemAdmin(admin.ModelAdmin):
    list_display = ("item_name", "item_type")
    list_filter = ("item_name", "item_type")
    search_fields = ("item_name", "item_type")


class MaintenanceTicketInline(admin.StackedInline):
    form = ticket_form
    model = Ticket
    extra = 1


@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ("maintenance_name", "maintenance_date", "maintenance_description")
    list_filter = ("maintenance_name", "maintenance_date", "maintenance_description")
    search_fields = ("maintenance_name", "maintenance_date")
    inlines = [MaintenanceTicketInline]


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    form = ticket_form
    list_display = ("ticket_no", "room")
    list_filter = ("ticket_no", "room")
    search_fields = ("ticket_no", "room")


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("id", "comments", "time")
    list_filter = ("id", "comments", "time")
    search_fields = ("id", "comments", "time")
    inlines = [ActivityItemInline]
