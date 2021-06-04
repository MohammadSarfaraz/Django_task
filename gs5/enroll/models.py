from django.db import models
from django.contrib.auth.models import User


# Create your models here.
STATE_CHOICES = (
    ('Andaman & Nicobar Island','Andaman & Nicobar Island'),
    ('Bihar','Bihar'),
    ('Assam','Assam'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Delhi','Delhi')
)
class Customer(models.Model):
    
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)
    
    def __str__(self):
        return str(self.id)
