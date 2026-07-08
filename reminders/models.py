from django.db import models
from tasks.models import Task
# Create your models here.


class Reminder(models.Model):
    task = models.OneToOneField(
        Task,
        on_delete= models.CASCADE
    )

    reminder_time= models.DateTimeField()
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return self.task.title
    