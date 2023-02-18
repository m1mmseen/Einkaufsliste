from django.db import models
from datetime import date

# Create your models here.
class ShoppingItem(models.Model):
    creatDate = models.DateField (default=date.today)
    name = models.CharField (max_length =200)
    done = models.BooleanField(default=False)

    def __str__(self):
        return '(' + str(self.id) +') ' +self.name