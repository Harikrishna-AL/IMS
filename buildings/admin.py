from django.contrib import admin

# Register your models here.
from .models import ( Building, Block, Floor, Room, Item,RoomItem, 
Department, Maintenance, Ticket )
from django.contrib import admin




@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'state','country')
    list_filter = ('state', 'country')
    search_fields = ('name', 'state', 'country')

@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('name', 'floors')
    list_filter = ('name', 'floors')
    search_fields = ('name', 'floors')

@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display = ('name', 'no_rooms')
    list_filter = ('name', 'no_rooms')
    search_fields = ('name', 'no_rooms')
    raw_id_fields = ('block',)

# @admin.register(RoomItem)
class RoomItemInline(admin.TabularInline):
    model=RoomItem
    extra=1

@admin.register(Room)
class roomsAdmin(admin.ModelAdmin):
    list_display = ('room_no', 'room_type')
    list_filter = ('room_type', 'room_no')
    raw_id_fields = ('floor',)
    search_fields = ('room_no', 'room_type')
    inlines=[RoomItemInline]

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(Item)
class itemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'item_type')
    list_filter = ('item_name', 'item_type')
    search_fields = ('item_name', 'item_type')

class MaintenanceTicketInline(admin.StackedInline):
    model=Ticket
    extra=1

@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('maintenance_name', 'maintenance_date','maintenance_description')
    list_filter = ('maintenance_name', 'maintenance_date', 'maintenance_description')
    search_fields = ('maintenance_name', 'maintenance_date')
    inlines = [MaintenanceTicketInline]

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_no', 'room')
    list_filter = ('ticket_no', 'room')
    search_fields = ('ticket_no', 'room')
    

# class EventAdminSite(admin.AdminSite):
#     def get_app_list(self, request):
#         """
#         Return a sorted list of all the installed apps that have been
#         registered in this site.
#         """
#         ordering = {
#             "Buildings": 1,
#             "Blocks": 2,
#             "Floors": 3,
#             "Rooms": 4,
#             "Items": 5,
#         }
#         app_dict = self._build_app_dict(request)
#         # a.sort(key=lambda x: b.index(x[0]))
#         # Sort the apps alphabetically.
#         app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

#         # Sort the models alphabetically within each app.
#         for app in app_list:
#             app['models'].sort(key=lambda x: ordering[x['name']])

#         return app_list