# importing the models we created so that they appear as tables to the admin site
from .models import Movies
from django.contrib import admin

# passing the model we ccreateed
admin.site.register(Movies)

