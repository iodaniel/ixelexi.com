from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import reverse



class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_id = models.CharField(max_length=255)
    stripe_subscription_id = models.CharField(max_length=255)
    cancel_at_period_end = models.BooleanField(default=False)
    membership = models.BooleanField(default=False)

    def __str__(self):
        return self.members


    @property
    def members(self):
        return '{}'.format(self.user)