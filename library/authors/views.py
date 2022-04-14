import random
import uuid

from django.shortcuts import render
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer, StaticHTMLRenderer, AdminRenderer, OrderedDict
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.views import APIView
from .models import Author, Book, Article, Biography
from .serializers import BookSerializer, AuthorSerializer, ArticleSerializer, BiographySerializer, \
    SimpleAuthorSerializer, CommentSerializer, SimpleBookSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from datetime import datetime


# Create your views here.

# Виды Renderers
# Полный список видов Renderers можно найти в разделе Renderers, официальной документации. Рассмотрим основные из них:
# 1.	JSONRenderer — преобразует данные в формат JSON.
# 2.	TemplateHTMLRenderer — преобразует данные в формат html. Используются html-шаблоны.
# 3.	StaticHTMLRenderer — преобразует данные в html без использования шаблонов, возвращает статическую html-разметку.
# 4.	BrowsableAPIRenderer — преобразует данные для удобной работы с API в брауезере.
# 5.	AdminRenderer — преобразует данные для удобного администрирования.


class AuthorApiView(APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer]

    def get(self, request):
        print(request.query_params)
        name = request.query_params['name']
        print(name)
        authors = Author.objects.filter(first_name__contains=name)
        # print(dir(request))
        serializer = AuthorSerializer(authors, many=True, context={'request': request})
        # print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        print(dir(request))
        print(request.data)
        return Response(request.data)


class AuthorModelViewSet(ModelViewSet):
    # если нужно, то в отдельных вьюхах можно выбирать нужный вид ренедра
    permission_classes = [IsAuthenticated]
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookModelViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            print('сработал')
            print(self.request.data, self.request.headers)
            return SimpleBookSerializer
        print('не сработал')
        return BookSerializer


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer



# Проработка
class Comment:
    def __init__(self, email, content, created=None, answ=None, book=None, book_name=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()
        self.answ = answ
        self.book = book
        self.g = uuid.uuid4()
        self.book_name = book_name

class answ:
    def __init__(self, answ, created=None):
        self.answ = answ
        self.created = created or datetime.now()
        self.modify = True
        self.randint = random.randint(1, 100)


class CommentView(ViewSet):
    permission_classes = [AllowAny]
    renderer_classes = [JSONRenderer]

    def list(self, request):
        print('test')
        book = Book.objects.all()
        # print(book.values())
        queryset = []
        for i in range(100):
            rint = random.randint(1, len(book))
            json_book = SimpleBookSerializer(book, many=True).data[max(rint-2, 0):rint]
            # book_name = SimpleBookSerializer(book)
            add_answ = answ(answ=f'данные {i}')
            comment = Comment(email='pavel-zh@inbox.ru', content='my tasks', answ=add_answ, book=json_book, book_name=book[1])
            queryset.append(comment)
        comment_serializer = CommentSerializer(instance=queryset, many=True)
        json = JSONRenderer().render(comment_serializer.data)
        print(json)
        print(type(comment_serializer))
        print(type(json))
        return Response(comment_serializer.data)


