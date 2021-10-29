from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Todo (models.Model):
    title= models.CharField(max_length=50)
    memo= models.TextField(blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    completedAt = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    todoCreator = models.ForeignKey(User, on_delete=models.CASCADE)
    # slug = models.SlugField

    class Meta:
        ordering= ['-createdAt']
        verbose_name= "Todo Lists"

    def __str__(self):
        return self.title