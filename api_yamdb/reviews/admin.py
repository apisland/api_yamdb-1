from django.contrib import admin

from .models import Category, Comment, Genre, GenreTitle, Reviews, Titles, User

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Titles)
admin.site.register(GenreTitle)
admin.site.register(Reviews)
admin.site.register(Comment)
