from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Author, Article, Biography, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        # fields = '__all__'
        fields = ['url', 'uid', 'first_name', 'last_name', 'birthday_year']


class BiographySerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Biography
        fields = ['text', 'author']


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Article
        exclude = ['name']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    authors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = '__all__'
