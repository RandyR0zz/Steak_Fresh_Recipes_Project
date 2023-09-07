from django.contrib import admin
from .models import Author, Post

# Adding Author model to the administration panel with fields
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['username', 'mail']


# Adding Post model to the administration panel with fields
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'moderation']