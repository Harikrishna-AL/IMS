from django.db import models

# Create your models here.
class rooms(models.Model):
    room_type = models.CharField(max_length=200)
    room_no = models.IntegerField()
    id = models.AutoField(primary_key=True)
    # block = models.ForeignKey(Block, on_delete=models.CASCADE)
    def __str__(self):
        return self.name    