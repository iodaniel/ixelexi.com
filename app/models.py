from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} | email: {self.email} | phone number:{self.phone_number} | message:{self.message}"
