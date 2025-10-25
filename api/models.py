from django.db import models

class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
