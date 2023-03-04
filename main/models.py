from django.db import models

class Task(models.Model):
    task = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self) :
        return self.task
