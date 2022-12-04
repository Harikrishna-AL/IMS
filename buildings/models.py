from django.db import models
import uuid
from django.core.exceptions import ValidationError

# Create your models here.


class Building(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200, default="state")
    zip = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Block(models.Model):

    name = models.CharField(max_length=200)
    floors = models.IntegerField()
    id = models.AutoField(primary_key=True)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True)

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
    item_type = models.CharField(
        max_length=100,
        null=True,
        help_text="Enter the item type (e.g. Fan, Tubelight Table, Chair, etc.)",
    )
    item_value = models.CharField(
        max_length=200, help_text="Enter item value(e.g. 40W)"
    )

    def __str__(self):
        return self.item_name


class Room(models.Model):
    room_no = models.IntegerField()
    id = models.AutoField(primary_key=True)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, null=True)
    room_type = models.CharField(max_length=100)
    items = models.ManyToManyField(
        Item, related_name="room_items", blank=True, through="RoomItem"
    )

    def __str__(self):
        return self.room_type

    def clean(self):
        room_no_floor = self.floor.no_rooms
        rooms_count = self.floor.room_set.all().count()
        if room_no_floor < rooms_count + 1:
            raise ValidationError("Floor Room Limit exceeded!")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class RoomItem(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)

    def __str__(self):

        return f"{self.item.item_name} X {self.count}"


class Maintenance(models.Model):
    MAINTENANCE_TYPE = (
        ("Daily", "Daily"),
        ("Weekly", "Weekly"),
        ("Monthly", "Monthly"),
        ("Quarterly", "Quarterly"),
        ("Half Yearly", "Half Yearly"),
        ("Yearly", "Yearly"),
    )
    id = models.AutoField(primary_key=True)
    maintenance_name = models.CharField(max_length=200)
    maintenance_date = models.DateField()
    maintenance_description = models.TextField()
    maintenance_type = models.CharField(
        max_length=200, choices=MAINTENANCE_TYPE, default="Daily"
    )

    def __str__(self):
        return self.maintenance_name


class Ticket(models.Model):
    ticket_no = models.UUIDField(default=uuid.uuid4, editable=False)
    department = models.ManyToManyField(
        Department, related_name="ticket_department", blank=True
    )
    room = models.CharField(max_length=100)
    message = models.TextField()  # about the maintenance
    maintenance = models.ForeignKey(Maintenance, on_delete=models.CASCADE, null=True)
    maintenance_tickets = models.ManyToManyField(
        Maintenance,
        related_name="maintenance_tickets",
        blank=True,
        through="MaintenanceTicket",
    )
    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Completed", "Completed"),
    )
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default="Pending")

    def __str__(self):
        return str(self.ticket_no)


class MaintenanceTicket(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    maintenance = models.ForeignKey(Maintenance, on_delete=models.CASCADE)

    count = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.maintenance.maintenance_name} X {self.count}"


class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    items = models.ManyToManyField(
        Item, related_name="activity_items", blank=True, through="ActivityItem"
    )
    comments = models.TextField()
    time = models.TimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Activities"

    def __str__(self):
        return str(self.id) + "#" + str(self.ticket.ticket_no)


class ActivityItem(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.items.item_name} X {self.count}"
