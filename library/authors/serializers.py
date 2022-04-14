import uuid

from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Author, Article, Biography, Book


class SimpleAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        # fields = '__all__'
        fields = ['id', 'url', 'first_name', 'last_name', 'birthday_year']


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        # fields = '__all__'
        fields = ['id', 'url', 'first_name', 'last_name', 'birthday_year']


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


class BookSerializer(serializers.ModelSerializer):
    # https: // www.django - rest - framework.org / api - guide / relations /
    # 1.	StringRelatedField — представляет объект методом __str__.
    # 2.	PrimaryKeyRelatedField — представляет объект его id (используется по умолчанию).
    # 3.	HyperlinkedRelatedField — представляет объект гипперссылкой. Обычно она ведёт на страницу detail этого объекта.
    # 4.	SlugRelatedField — позволяет указать несколько полей для отображения объекта.
    # authors = serializers.StringRelatedField(many=True)
    # authors = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # authors = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='AuthorModelViewSet')
    authors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = '__all__'


class SimpleBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AnswSerializers(serializers.Serializer):
    answ = serializers.CharField(max_length=126)
    created = serializers.DateTimeField()
    modify = serializers.BooleanField()
    randint = serializers.IntegerField()

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
    g = serializers.UUIDField(default=uuid.uuid4())
    answ = AnswSerializers()
    book = serializers.JSONField()
    book_name = serializers.CharField(source='book_name.name', max_length=100)
