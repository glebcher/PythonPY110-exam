import random
from random import randint
import json
import linecache
from conf import MODEL
from faker import Faker
faker = Faker()
# Faker.seed(0)

model = MODEL
pk = 1


with open('books.txt') as f:
    count = sum(1 for _ in f)


def book_line_gen():
    book_line = randint(0, count - 1)
    return book_line


def book_title_gen():
    book_title = linecache.getline('books.txt', book_line_gen())
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


def book_gen(pk=1):
    while True:
        yield {"model": model,
               "pk": pk,
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
        pk += 1


list_books = []


def main():
    book_generator = book_gen()

    for _ in range(100):
        list_books.append(next(book_generator))


def _json():
    jsonString = json.dumps(list_books, indent=4, ensure_ascii=False)
    jsonFile = open("data.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()


if __name__ == "__main__":
    main()
    _json()
    print(count)