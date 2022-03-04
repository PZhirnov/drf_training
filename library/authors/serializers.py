from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Author, Article, Biography, Book


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        # fields = '__all__'
        fields = ['url', 'uid', 'first_name', 'last_name', 'birthday_year']


class BiographySerializer(serializers.HyperlinkedModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Biography
        fields = ['text', 'author']


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Article
        exclude = ['name']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    # https: // www.django - rest - framework.org / api - guide / relations /
    # 1.	StringRelatedField — представляет объект методом __str__.
    # 2.	PrimaryKeyRelatedField — представляет объект его id (используется по умолчанию).
    # 3.	HyperlinkedRelatedField — представляет объект гипперссылкой. Обычно она ведёт на страницу detail этого объекта.
    # 4.	SlugRelatedField — позволяет указать несколько полей для отображения объекта.

    # authors = serializers.StringRelatedField(many=True)
    # authors = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # authors = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='AuthorModelViewSet')
    class Meta:
        model = Book
        fields = '__all__'
