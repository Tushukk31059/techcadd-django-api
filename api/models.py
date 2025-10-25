from django.db import models

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name
