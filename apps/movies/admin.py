from django.contrib import admin
from .models import Movie, Actor, Genre, Review, Trailer,View

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Trailer)
admin.site.register(View)