from django.db import models

# Create your models here.

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    email =  models.CharField(max_length=100)
    test_score1 = models.IntegerField()
    test_score2 = models.IntegerField()
    test_score3 = models.IntegerField()
    
