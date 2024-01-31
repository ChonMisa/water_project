from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    image = models.ImageField(upload_to='task_images/', blank=True, null=True)

    def __str__(self):
        return self.title
