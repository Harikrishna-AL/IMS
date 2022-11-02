from django.db import models
from room.models import rooms
# Create your models here.
class items(models.Model):
    item_name = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)
    item_value = models.IntegerField()
    room = models.ForeignKey(rooms, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name