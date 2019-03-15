from django.db import models

class Site(models.Model):
    Title = models.CharField('Movie title', max_length=40, null="False", default="Title")
    Year = models.CharField('Year', max_length=4, null=True)
    Rating = models.IntegerField(null=True)
    
    def __str__(self):
        return self.Title