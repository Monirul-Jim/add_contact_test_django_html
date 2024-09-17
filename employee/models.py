from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField()
    address = models.TextField()

    def __str__(self):
        return self.first_name
