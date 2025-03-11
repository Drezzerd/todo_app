from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        (1, "Faible"),
        (2, "Moyenne"),
        (3, "Haute"),
    ]

    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.get_priority_display()}"
