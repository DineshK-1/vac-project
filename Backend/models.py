from django.db import models

class BackendModel(models.Model):
    username = models.CharField(max_length=100)
    Text = models.TextField()
    Date = models.DateTimeField(auto_now_add=True, null = True, blank = True)