# these are like the tables we are gonna have at the admin site
from django.db import models

#create a model class to decribe our movies 
class Movies(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField(default=2000)

    # overwriting the default display of the admin string descriptions
    def __str__(self):
        return f'{self.title} from {self.year}'
