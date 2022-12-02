from django.db import models
import uuid
from django.core.exceptions import ValidationError
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
    name = models.CharField(max_length=200)
    floors = models.IntegerField()
    id = models.AutoField(primary_key=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name

class Floor(models.Model):
    name = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)
    no_rooms = models.IntegerField()
    block = models.ForeignKey(Block, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    item_type = models.CharField(max_length = 100, null=True, 
            help_text= 'Enter the item type (e.g. Fan, Tubelight Table, Chair, etc.)')
    item_value = models.CharField(max_length=200, help_text='Enter item value(e.g. 40W)')

    # def get_department(self):
    #     return Department.objects.values_list('name', flat=True).values()
    # room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    # def generate_GenderChoices():
    #     choice = ()
    #     for department in Department.objects.values_list('name', flat=True).values():
    #         item_choice = ()
    #         for item in department.:
    #             item_choice += (item, item)
    #         choice += (department, item_choice)
    # GENRE_CHOICES = (
    # ('Electrical', (
    #     ('Fan', 'Fan'),
    #     ('TubeLight', 'TubeLight'),
    #     ('Bulb', 'Bulb'),
    #     ('Other', 'Other')

    # )),
    # ('Plumbing', (
    #     ('Flush', 'Flush'),
    #     ('Tank', 'Tank'),
    #     ('Taps', 'Taps'),
    #     ('Other', 'Other'),
    #     )),
    # ('Furniture', (
    #     ('Chair', 'Chair'),
    #     ('Table', 'Table'),
    #     ('Other', 'Other'),
    #     )), 
    # )

    def __str__(self):
        return self.item_name

class Room(models.Model):
    room_no = models.IntegerField()
    id = models.AutoField(primary_key=True)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, null=True)
    # GENRE_CHOICES = (
    #     ('Office', 'Office'),
    #     ('Lab', 'Lab'),
    #     ('Ward', (
    #         ('Multibed Ward', 'Multibed Ward'),
    #         ('Single Bed Ward', 'Single Bed Ward'),
    #         ('Twin Sharing Room','Twin Sharing Room'),
    #         ('Single Room', 'Single Room'),
    #         ('Single Deluxe Room', 'Single Deluxe Room'),
    #         ('Super Deluxe Room', 'Super Deluxe Room'),
    #         ('Suite', 'Suite'),
    #     )),
    #     ('Store', 'Store'),
    #     ('Other', 'Other'),
    #     )
    room_type = models.CharField(max_length=100)
    items=models.ManyToManyField(Item, related_name='room_items',blank=True,through='RoomItem')

    def __str__(self):
        return self.room_type

    def clean(self):
        room_no_floor=self.floor.no_rooms
        rooms_count=self.floor.room_set.all().count()
        if room_no_floor < rooms_count+1:
            raise ValidationError("Floor Room Limit exceeded!")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

# class RoomItem(models.Model):
#     room=models.ForeignKey(Room,on_delete=models.CASCADE)
#     item=models.ForeignKey(Item,on_delete=models.CASCADE)
#     activity=models.ForeignKey(Activity,on_delete=models.CASCADE)
#     count=models.IntegerField(default=1)

#     def __str__(self):
        
#         return f"{self.item.item_name} X {self.count}"


class Maintenance(models.Model):
    MAINTENANCE_TYPE = (
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
        ('Half Yearly', 'Half Yearly'),
        ('Yearly', 'Yearly'),
    )
    id = models.AutoField(primary_key=True)
    maintenance_name = models.CharField(max_length=200)
    maintenance_date = models.DateField()
    maintenance_description = models.TextField()
    maintenance_type = models.CharField(max_length=200, choices=MAINTENANCE_TYPE, default='Daily')
    def _str_(self):
        return str(self.maintenance_date)

class Ticket(models.Model):
    ticket_no = models.UUIDField(default=uuid.uuid4, editable=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    room = models.CharField(max_length=100)
    message = models.TextField()  #about the maintenance
    maintenance = models.ForeignKey(Maintenance, on_delete=models.CASCADE, null=True)

    def _str_(self):
        return str(self.ticket_no)
        
class RoomItem(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    # activity=models.ForeignKey(Activity,on_delete=models.CASCADE)
    count=models.IntegerField(default=1)
    

    def __str__(self):
        return f"{self.item.item_name} X {self.count}"

class Activity(models.Model):
    id=models.AutoField(primary_key=True)
    ticket=models.ForeignKey(Ticket,on_delete=models.CASCADE)
    items=models.ManyToManyField(Item, related_name='activity_items',blank=True,through='ActivityItem')
    comments = models.TextField()
    time=models.TimeField(auto_now=True)

    def __str__(self):
        return str(self.id)+"#"+str(self.ticket.ticket_no)

class ActivityItem(models.Model):
    activity=models.ForeignKey(Activity,on_delete=models.CASCADE)
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    time=models.TimeField
    def __str__(self):
        return self.item