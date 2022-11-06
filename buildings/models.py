from django.db import models
# import django_filters
from django.contrib import admin
# Create your models here.
class Building(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200, default='state')
    zip = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.name



class Block(models.Model):
    # uid = models.Field(primary_key=1)
    name = models.CharField(max_length=200)
    floors = models.IntegerField()
    id = models.AutoField(primary_key=True)
    buildingId = models.ForeignKey(Building, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name

class Floor(models.Model):
    name = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)
    no_rooms = models.IntegerField()
    block = models.ForeignKey(Block, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

class room(models.Model):
    room_type = models.CharField(max_length=200)
    room_no = models.IntegerField()
    id = models.AutoField(primary_key=True)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.room_type

class item(models.Model):
    item_name = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)
    item_value = models.IntegerField()
    room = models.ForeignKey(room, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.item_name