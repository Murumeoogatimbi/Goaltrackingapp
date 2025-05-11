from django.db import models

class Goal(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True,null=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-is_completed"]

