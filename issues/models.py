from django.db import models
from django.contrib.auth.models import get_user_model

User = get_user_model()


class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=256)

    def __str__(self):
        return self.name
    
class Priority(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=256)

    def __str__(self):
        return self.name
    

class Issue(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.ForeignKey(
        'Status', 
        on_delete=models.SET_NULL, 
        null=True
    )
    priority = models.ForeignKey(
        'Priority', 
        on_delete=models.SET_NULL, 
        null=True
    )
    reporter = models.ForeignKey(
        get_user_model(),  # ✅ Explicit call for clarity
        on_delete=models.SET_NULL,
        null=True,
        related_name='reporter'
    )
    assignee = models.ForeignKey(
        get_user_model(),  # ✅ Explicit call for clarity
        on_delete=models.SET_NULL,
        null=True,
        related_name='assignee'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

# reporter = models.ForeignKey(
#    get_user_model(),
#    on_delete=models.SET_NULL,
#    related_name='reporter',