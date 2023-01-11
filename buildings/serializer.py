from rest_framework import serializers
from .models import Ticket, Department, Room

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ticket
        fields=('ticket_no','department','room','message','maintenance','created_at','created_by','agents_assigned','status')

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=('id','name')

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields=('id','room_no','floor','room_type','items')