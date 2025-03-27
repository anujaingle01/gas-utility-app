from django.db import models
from users.models import CustomUser

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='requests')
    request_type = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='service_requests/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.request_type} - {self.customer.username}"
