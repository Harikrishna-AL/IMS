from django.db import models
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



class Item(models.Model):
    item_name = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)
    item_value = models.IntegerField()
    # room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    GENRE_CHOICES = (
    ('Electrical', (
        ('Fan', 'Fan'),
        ('TubeLight', 'TubeLight'),
        ('Bulb', 'Bulb'),
        ('Other', 'Other')

    )),
    ('Plumbing', (
        ('Flush', 'Flush'),
        ('Tank', 'Tank'),
        ('Taps', 'Taps'),
        ('Other', 'Other'),
        )),
    ('Furniture', (
        ('Chair', 'Chair'),
        ('Table', 'Table'),
        ('Other', 'Other'),
        )), 
    )

    item_type = models.CharField(max_length = 100, choices=GENRE_CHOICES, null=True)
    def __str__(self):
        return self.item_name

class Room(models.Model):
    room_no = models.IntegerField()
    id = models.AutoField(primary_key=True)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, null=True)
    GENRE_CHOICES = (
        ('Office', 'Office'),
        ('Lab', 'Lab'),
        ('Ward', (
            ('Multibed Ward', 'Multibed Ward'),
            ('Single Bed Ward', 'Single Bed Ward'),
            ('Twin Sharing Room','Twin Sharing Room'),
            ('Single Room', 'Single Room'),
            ('Single Deluxe Room', 'Single Deluxe Room'),
            ('Super Deluxe Room', 'Super Deluxe Room'),
            ('Suite', 'Suite'),
        )),
        ('Store', 'Store'),
        ('Other', 'Other'),
        )
    room_type = models.CharField(max_length=200, choices=GENRE_CHOICES)
    items=models.ManyToManyField(Item, related_name='room_items',blank=True,through='RoomItem')

    def __str__(self):
        return self.room_type

class RoomItem(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    count=models.IntegerField(default=1)

class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    ticket_no = models.IntegerField()
    # department = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    department = models.CharField(max_length=100)
    # room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    room = models.CharField(max_length=100)
    message = models.TextField()  #about the maintenance

    def _str_(self):
        return str(self.ticket_no)


class Maintenance(models.Model):
    id = models.AutoField(primary_key=True)
    # item = models.CharField(max_length=100)
    maintenance_date = models.DateField()
    maintenance_description = models.TextField()
    def _str_(self):
        return str(self.maintenance_date)