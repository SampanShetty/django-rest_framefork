from django.db import models

# Create your models here.


class User(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    age=models.IntegerField()
    height=models.FloatField()

    def __str__(self):
        return self.username
    