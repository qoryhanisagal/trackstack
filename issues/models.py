from django.db import models

class Issue(models.Model):
    STATUS_CHOICES = [
        ('backlog', 'Backlog'),
        ('ready', 'Ready'),
        ('in_progress', 'In Progress'),
        ('in_review', 'In Review'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='backlog')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title