from django.db import models
import random

def randomid():
    return str(random.randint(100000, 999999))

class Item(models.Model):
    itemid = models.CharField(default=randomid, max_length=6, unique=True)
    itemname = models.CharField(max_length=120)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)