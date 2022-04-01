from django.core.management import BaseCommand
from authors.models import Author, Book


AUTHORS = [
    {'first_name': 'Константин',
     'last_name': 'Аксаков',
     'birthday_year': 1892,
     'books': [
         'Аленький цветочек',
         'Семейная хроника',
         'Буран',
     ]
     },
    {'first_name': 'Анна',
     'last_name': 'Ахматова',
     'birthday_year': 1889,
     'books': [
         'Реквием',
         'Сероглазый король',
         'Мужество',
     ]
     },
    {'first_name': 'Александр',
     'last_name': 'Блок',
     'birthday_year': 1880,
     'books': [
         'Двенадцать',
         'Скифы',
         'Незнакомка',
         'Стихи о прекрасной даме',
     ]
     },
    {'first_name': 'Александр',
     'last_name': 'Пушкин',
     'birthday_year': 1799,
     'books': [
         'Евгений Онегин',
         'Капитанская дочка',
         'Пиковая дама',
         'Дубровский',
     ]
     },
    {'first_name': 'Лев',
     'last_name': 'Толстой',
     'birthday_year': 1828,
     'books': [
         'Анна Каренина',
         'После бала',
         'Война и мир',
         'Кавказский пленник',
     ]
     },
    {'first_name': 'Иван',
     'last_name': 'Тургенев',
     'birthday_year': 1818,
     'books': [
         'Отцы и дети',
         'Муму',
         'Ася',
         'Первая любовь',
     ]
     },
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        for author in AUTHORS:
            add_author = Author(first_name=author.get('first_name'),
                                last_name=author.get('last_name'),
                                birthday_year=author.get('birthday_year'))
            add_author.save()

            for book in author.get('books'):
                book = Book(name=book)
                book.save()
                book.authors.add(add_author)
                # book.save()







