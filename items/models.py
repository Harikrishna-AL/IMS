from django.db import models

# Create your models here.
class items(models.Model):
    item_name = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)
    item_value = models.IntegerField()
    def __str__(self):
        return self.name