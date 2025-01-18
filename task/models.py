from django.db import models

# Create your models here.
class TaskModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images")
    deadline = models.DateField()