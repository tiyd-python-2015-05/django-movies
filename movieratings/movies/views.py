from django.shortcuts import render

# Create your views here.
from .models import Movie
from django.db.models import Avg, Count


def all_movies(request):
    top_10_movies = Movie.objects.annotate(
        rating_count=(Count('rating__rating')),
        avg_rating=(Avg('rating__rating'))
    ).filter(rating_count__gte=10).order_by('-avg_rating')[:10]
    return render(request, 'movies/index.html', {"movies": top_10_movies})
