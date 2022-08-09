from django.http import HttpResponse
from django.shortcuts import render
# importing the models so that we display them from the admin site to the front end
from .models import Movies

# movie view
def movies(request):
    # we are getting all the movies from the model part
    data = Movies.objects.all()
    return render(request, 'movies/movies.html', {'movies':data})

# home page view
def home(request):
    return HttpResponse("Home page")

# movie description view
def detail(request, id):
    data = Movies.objects.get(pk=id)
    return render(request, 'movies/details.html', {'movie': data})

# adding the movie from the homepage view
def add(request):
    return render(request, 'movies/add.html')