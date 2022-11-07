from django.contrib import admin

# Register your models here.
from .models import Building, Block, Floor, Room, Item
from django.contrib import admin
# admin.site.register(Building)
@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'state','country')
    list_filter = ('state', 'country')

@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('name', 'floors')
    list_filter = ('name', 'floors')

@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display = ('name', 'no_rooms')
    list_filter = ('name', 'no_rooms')

@admin.register(Room)
class roomsAdmin(admin.ModelAdmin):
    list_display = ('room_type', 'room_no')
    list_filter = ('room_type', 'room_no')

@admin.register(Item)
class itemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'item_value', 'item_type')
    list_filter = ('item_name', 'item_value', 'item_type')

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
        # a.sort(key=lambda x: b.index(x[0]))
        # Sort the apps alphabetically.
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        # Sort the models alphabetically within each app.
        for app in app_list:
            app['models'].sort(key=lambda x: ordering[x['name']])

        return app_list