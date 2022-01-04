from django.db import models

class FrontendModels(models.Model):
    Category_List = [
        ("1", "HTML"),
        ("2", "CSS"),
        ("3", "JS"),
    ]

    Type = models.CharField(max_length=1, choices=Category_List)
    Title = models.CharField(max_length = 200, primary_key = True)
    Description = models.FileField()
