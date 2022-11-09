from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from . models import CustomUser, agent, customer
from . models import AgentUser, CustomerUser
# Register your models here.

@admin.register(AgentUser)
class AgentAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'phone', 'email']
    list_filter = ['name', 'username', 'phone', 'email']
    search_fields = ['name', 'username', 'phone', 'email']

@admin.register(CustomerUser)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'username', 'phone', 'email']
    list_filter = ['first_name', 'username', 'phone', 'email']
    search_fields = ['first_name', 'username', 'phone', 'email']