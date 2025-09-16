from django.contrib import admin
from .models import BookInstance, Book, Author, Genre
from django.contrib.admin import ModelAdmin, register

"""
    Model admin is used to add/change model behaviour on the admin site
    @admin.register(modelname) does the same thing as admin.sites.register which is to simply register models to the admin site/Dashboard
"""
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ["status", "due_back"]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
   list_display = ["title", "isbn", "language"]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "date_of_birth", "date_of_death"]
    fields = ["first_name", "last_name", ("date_of_birth", "date_of_death")]

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


# Register your models here.
# admin.site.register(BookInstance)
# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(Genre)




