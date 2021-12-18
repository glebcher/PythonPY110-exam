import random
from random import randint
import json
import linecache
from conf import MODEL
from faker import Faker
faker = Faker()
model = MODEL
pk = 1


def book_title_gen():
    f = open('books.txt')
    data = f.read()
    lines = data.split('\n')
    line = random.randrange(len(lines))
    book_title = lines[line]
    return book_title


def year_gen():
    year = randint(1900, 2010)
    return year


def pages_gen():
    pages = randint(150, 300)
    return pages


def rating_gen():
    rating = random.uniform(0.0, 5.1)
    return rating


def price_gen():
    price = random.uniform(1.0, 25.6)
    return price


def isbn13_gen():
    isbn13 = faker.isbn13()
    return isbn13


def author_gen():
    author = faker.name()
    return author


def book_gen(k=1):
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


def main():
    book_generator = book_gen()

    for _ in range(100):
        list_books.append(next(book_generator))


def _json():
    with open("data.json", "w") as file:
        json.dump(list_books, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
    _json()
