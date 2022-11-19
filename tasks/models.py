from django.db import models
from authentication.models import CustomUser


class Task(models.Model):
    class Priorities(models.TextChoices):
        HIGH = 'HI', 'HIGH'
        MEDIUM = 'ME', 'MEDIUM'
        LOW = 'LO', 'LOW'
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=150, null=False)
    description = models.TextField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=2,
                            choices=Priorities.choices,
                            default=Priorities.LOW)

    def __str__(self):
        return f"{self.title} {self.user}"
    
