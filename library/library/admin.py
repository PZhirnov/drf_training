from django.contrib import admin
from authors.models import Author
from authapp.models import LibUser
# Register your models here.

admin.site.register(Author)
admin.site.register(LibUser)
