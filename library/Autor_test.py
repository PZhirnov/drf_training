from rest_framework import serializers
from uuid import uuid4

# Описание классов модели
class Author:

    def __init__(self, name, birthday_year):
        self.name = name
        self.birthday_year = birthday_year

    def __str__(self):
        return self.name


class Biography:

    def __init__(self, text, author):
        self.author = author
        self.text = text


class Book:

    def __init__(self, name, authors):
        self.name = name
        self.authors = authors


class Article:

    def __init__(self, name, author, uid=None):
        self.name = name
        self.author = author
        self.uid = uuid4()

# Использование сериализаторов
class AuthorSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    birthday_year = serializers.IntegerField()

class ArticleSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    uid = serializers.UUIDField()
    author = AuthorSerializers()

# Создание автора
author = Author('Павел', 1998)
serializers = AuthorSerializers(author)
print(serializers.data)

# Cоздание статьи
article = Article('Как делать цветы', author)
serializers_article = ArticleSerializers(article)
print(serializers_article.data)
