from django.db import models
from django.contrib.auth.models import User
from categories.models import Category

# Create your models here.


class Task(models.Model):
    PRIORITY = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    title= models.CharField(max_length=200)
    description = models.TextField(blank=True)

    date = models.DateField()
    time = models.TimeField()

    priority = models.CharField(
        max_length=10, 
        choices= PRIORITY, 
        default='Medium'
    )

    completed = models.BooleanField(default=False)
    

    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category,
        on_delete= models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    