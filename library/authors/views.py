from django.shortcuts import render
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, StaticHTMLRenderer, AdminRenderer
from rest_framework.viewsets import ModelViewSet
from .models import Author, Book, Article, Biography
from .serializers import BookSerializer, AuthorSerializer, ArticleSerializer, BiographySerializer

# Create your views here.

# Виды Renderers
# Полный список видов Renderers можно найти в разделе Renderers, официальной документации. Рассмотрим основные из них:
# 1.	JSONRenderer — преобразует данные в формат JSON.
# 2.	TemplateHTMLRenderer — преобразует данные в формат html. Используются html-шаблоны.
# 3.	StaticHTMLRenderer — преобразует данные в html без использования шаблонов, возвращает статическую html-разметку.
# 4.	BrowsableAPIRenderer — преобразует данные для удобной работы с API в брауезере.
# 5.	AdminRenderer — преобразует данные для удобного администрирования.



class AuthorModelViewSet(ModelViewSet):
    # если нужно, то в отдельных вьюхах можно выбирать нужный вид ренедра
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer
