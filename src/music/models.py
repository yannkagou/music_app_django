from django.db import models
from django.conf import settings



class Subscriber(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True)

    class Meta:
        ordering = ['user__first_name', 'user__last_name']

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"
