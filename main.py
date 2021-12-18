import random
"""Импортируем модуль random для получаения случайных чисел"""
from random import randint
"""Модуль для возвращения случайного целого числа"""
import json
"""Модуль для кодирования данных в json формате """
from conf import MODEL
"""Импортируем переменную MODEL из файла conf"""
from faker import Faker
"""Модуль Faker для получения случайных данных заданного формата"""
faker = Faker()
model = MODEL
pk = 1


def book_title_gen() -> str:
    """Читает файл books.txt, вовзращает случайную строку"""
    f = open('books.txt')
    data = f.read()
    lines = data.split('\n')
    line = random.randrange(len(lines))
    book_title = lines[line]
    return book_title


def year_gen() -> int:
    """Возвращает случайное целое число"""
    year = randint(1900, 2010)
    return year


def pages_gen() -> int:
    """Возвращает случайное целое число"""
    pages = randint(150, 300)
    return pages


def rating_gen() -> float:
    """Возвращает случайное число с плавующей точкой"""
    rating = random.uniform(0.0, 5.1)
    return rating


def price_gen() -> float:
    """Возвращает случайное число с плавующей точкой"""
    price = random.uniform(1.0, 25.6)
    return price


def isbn13_gen() -> str:
    """Возвращает строку, генерируемую модулем Faker"""
    isbn13 = faker.isbn13()
    return isbn13


def author_gen() -> str:
    """Возвращает строку, генерируемую модулем Faker"""
    author = faker.name()
    return author


def book_gen(k=1) -> dict:
    """Возвращает словарь"""
    while True:
        yield {"model": model,
               "pk": k,
               "fields": {
                   "title": book_title_gen(),
                   "year": year_gen(),
                   "pages": pages_gen(),
                   "isbn13": isbn13_gen(),
                   "rating": rating_gen(),
                   "price": price_gen(),
                   "author": author_gen()
               }
               }
        k += 1


list_books = []


def main() -> list:
    """Возвращает список словарей"""
    book_generator = book_gen()

    for _ in range(100):
        list_books.append(next(book_generator))


def _json() -> json:
    """Возвращает список json формата"""
    with open("data.json", "w") as file:
        json.dump(list_books, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
    _json()
