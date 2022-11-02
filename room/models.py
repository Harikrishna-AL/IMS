from django.db import models
from floors.models import Floor 

# Create your models here.
class rooms(models.Model):
    room_type = models.CharField(max_length=200)
    room_no = models.IntegerField()
    id = models.AutoField(primary_key=True)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.room_type