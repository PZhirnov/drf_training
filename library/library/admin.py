from django.contrib import admin
from authors.models import Author, Book, Biography, Article
from authapp.models import LibUser
# Register your models here.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Biography)
admin.site.register(Article)
admin.site.register(LibUser)
