from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# from phonenumber_field.modelfields import PhoneNumberField

SERVICE_CHOICE = (
    ("HIFU Face", "HIFU Face"),
    ("HIFU Body", "HIFU Body"),
    ("HIFU Vagin", "HIFU Vagin"),
)

TIME_CHOICE=(
    ("10:00 AM", "11:00 AM"),
    ("11:00 AM", "11:00 AM"),
    ("12:00 PM", "12:00 PM"),
    ("1:00 PM", "1:00 PM"),
    ("3:00 PM", "3:00 PM"),
    ("4:00 PM", "4:00 PM"),
    ("5:00 PM", "5:00 PM"),
    ("6:00 PM", "6:00 PM"),

)
      
class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICE, default="HIFU Face")
    # phone = PhoneNumberField(null=False, blank=False, unique=True)
    # day = models.DateField(default=datetime.now())
    day = models.DateField(default=datetime.now())
    time = models.CharField(max_length=10, choices=TIME_CHOICE, default="10:00 AM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return f"{self.user.username} | day: {self.day} |time:{self.time} | service:{self.service}"

# Create your models here.
