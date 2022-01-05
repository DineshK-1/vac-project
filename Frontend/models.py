from django.db import models



class FrontendModels(models.Model):
    def ReturnType(self, filename):
        return f'{self.Type}/{filename}'
    Category_List = [
        ("HTML", "HTML"),
        ("CSS", "CSS"),
        ("JS", "JS"),
    ]

    Type = models.CharField(max_length=4, choices=Category_List)
    Title = models.CharField(max_length = 200, primary_key = True)
    Description = models.FileField(upload_to = ReturnType)