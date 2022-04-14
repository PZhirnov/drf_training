import graphene
from graphene_django import DjangoObjectType
from authors.models import Author, Book
from graphene import String, Schema
from datetime import datetime


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields ='__all__'


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'


class TestType(DjangoObjectType):
    s = 15
    class Meta:
        model = Book
        fields = '__all__'


class AuthorMutation(graphene.Mutation):
    class Arguments:
        birthday_year = graphene.Int(required=True)
        id = graphene.ID()

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, birthday_year, id):
        author = Author.objects.get(pk=id)
        author.birthday_year = birthday_year
        author.save()
        return AuthorMutation(author=author)


class Mutation(graphene.ObjectType):
    update_author = AuthorMutation.Field()


class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    all_authors = graphene.List(AuthorType)
    author_by_id = graphene.Field(AuthorType, id=graphene.Int(required=True))
    books_by_author_name = graphene.List(BookType, name=graphene.String(required=False))
    # info_val = String(time=String(default_value=datetime.now()))
    info_val = graphene.List(TestType)

    def resolve_info_val(root, info):
        books = Book.objects.all()[:10]
        return books

    def resolve_all_books(root, info):
        books = Book.objects.all()
        return books.order_by('name')

    def resolve_all_authors(root, info):
        authors = Author.objects.all()
        return authors.order_by('first_name')

    def resolve_author_by_id(self, info, id):
        try:
            return Author.objects.get(id=id)
        except Author.DoesNotExist:
            return None

    def resolve_books_by_author_name(self, info, name=None):
        books = Book.objects.all()
        if name:
            books = books.filter(authors__first_name__icontains=name)
        return books


schema = graphene.Schema(query=Query, mutation=Mutation)
