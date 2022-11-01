from django.db import models

# Create your models here.
class Floor(models.Model):
    name = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)
    no_rooms = models.IntegerField()
    # block = models.ForeignKey(Block, on_delete=models.CASCADE)
    def __str__(self):
        return self.name