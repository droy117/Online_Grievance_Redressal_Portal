from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone_number = models.IntegerField(default=0)
    address = models.CharField(max_length=500, default="No Value")
    state = models.CharField(max_length=100, default="No Value")
    gender = models.CharField(max_length=50, default="No Value")

class GrievanceCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class GrievanceStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Grievance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='grievances')
    grievance_text = models.TextField()
    grievance_against = models.CharField(max_length=200)
    categories = models.ManyToManyField(GrievanceCategory, related_name='grievances')
    status = models.ForeignKey(GrievanceStatus, on_delete=models.CASCADE, related_name='grievances')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Grievance #{self.id} - {self.grievance_against}"

class GrievanceAction(models.Model):
    ACTION_CHOICES = (
        ('Assigned', 'Assigned'),
        ('Resolved', 'Resolved'),
        ('Reopened', 'Reopened'),
        # Add more action types as needed
    )

    grievance = models.ForeignKey(Grievance, on_delete=models.CASCADE, related_name='actions')
    action_type = models.CharField(max_length=20, choices=ACTION_CHOICES)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action_type} on Grievance #{self.grievance.id}"

