from django.db import models

from buildings.models import Building

# Create your models here.
class Block(models.Model):
    name = models.CharField(max_length=200)
    floors = models.IntegerField()
    id = models.AutoField(primary_key=True)
    buildingId = models.ForeignKey(Building, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name