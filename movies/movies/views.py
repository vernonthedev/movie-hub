from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
# importing the models so that we display them from the admin site to the front end
from .models import Movies

# movie view
def movies(request):
    # we are getting all the movies from the model part
    data = Movies.objects.all()
    return render(request, 'movies/Movie-Library.html', {'movies':data})

# home page view
def home(request):
    return render(request, 'movies/Home.html')

# movie description view
def detail(request, id):
    data = Movies.objects.get(pk=id)
    return render(request, 'movies/details.html', {'movie': data})

# adding the movie from the homepage view
def add(request):
    # get the data submitted through the form 
    title = request.POST.get('title')
    year = request.POST.get('year')
    desc = request.POST.get('movie_description')
    # if statements send the data and render it by creating a new object
    if title and year and desc:
        # create a new object
        movie =  Movies(title=title, year=year, description=desc)
        movie.save()
        return HttpResponseRedirect('/movies')
    return render(request, 'movies/create-movie-library.html')

# creating the delete view 
def delete(request, id):
    try:
        movie = Movies.objects.get(pk=id)
    except: 
        raise Http404("Movie Does not Exist")
    movie.delete()
    return HttpResponseRedirect('/movies')

# creating a login view
def loghere(request):
    return render(request, 'movies/logme.html')

# creating a login view
def createlib(request):
    return render(request, 'movies/create-movie-library.html')
