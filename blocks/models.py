from django.db import models

# Create your models here.
class Block(models.Model):
    name = models.CharField(max_length=200)
    floors = models.IntegerField()
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.name