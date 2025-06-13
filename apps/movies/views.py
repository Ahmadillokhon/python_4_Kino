from django.shortcuts import render,redirect
from .models import Movie,Review, Genre
from django.urls import reverse
from django.db.models import Avg



def movies_views(request):
    search = request.GET.get('search')
    genres = Genre.objects.all()
    genre_id = request.GET.get('genre')


    movies = Movie.objects.all()


    if genre_id:
        movies = movies.filter(genres__name=genre_id)


    if search:
        movies = Movie.objects.filter(title__icontains=search)


    return render(request, "movies.html",{"movies":movies, 'Genres':genres, 'selected_genre':genre_id })



def movie_view(request, pk):
    movie = Movie.objects.get(id=pk)
    rating_data = Review.objects.filter(movie=movie).aggregate(Avg('rating'))
    avg_rating = rating_data['rating__avg']
    if avg_rating:
        avg_rating = round(avg_rating, 1)
    
    return render(request, 'movie.html', context={
        'movie': movie,
        'rating': avg_rating,
        'reviews': movie.review_set.all(),
        'genres': Genre.objects.all(),
    })



def add_review_view(request,pk):
    comment = request.POST.get('comment')
    rating = request.POST.get('rating')
    name =  request.POST.get('name')
    email = request.POST.get('email')
    movie = Movie.objects.get(id = pk)

    Review.objects.create(
    rating = rating,
    comment = comment,
    name =  name,
    email = email,
    movie = movie,
    )

    return redirect(reverse('movie', kwargs={'pk': pk}))

