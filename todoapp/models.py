from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    priority = models.CharField(max_length=10, choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')])
    due_date = models.DateField(null=True, blank=True)
    notes = models.CharField(max_length=500, null=True, blank=True)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title