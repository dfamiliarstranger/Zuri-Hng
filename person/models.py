# from django.db import models

# class Person(models.Model):
#     name = models.CharField(max_length=100,unique=True)
#     # first_name = models.CharField(max_length=100,unique=True)
#     # last_name = models.CharField(max_length=100, unique=True)
#     # age = models.PositiveIntegerField()
   
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=255, unique=True)  # Example field definition
    # Other fi

    def __str__(self):
        return self.first_name
