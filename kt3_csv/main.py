from pathlib import Path


def _parse_row(line):
    isbn, title, author, quantity, price = line.rstrip("\n").split("|")
    return [isbn, title, author, int(quantity), float(price)]


def get_books(filename):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.read().splitlines()
    header = lines[0].split("|")
    rows = list(map(_parse_row, filter(None, lines[1:])))
    return [header] + rows


def filtered_books(books, text):
    search_text = text.casefold()
    matches = filter(lambda book: search_text in book[1].casefold(), books[1:])
    return list(map(lambda book: [book[0], book[1] + ", " + book[2], book[3], book[4]], matches))


def books_value(books):
    return list(map(lambda book: (book[0], book[3] * book[4]) if len(book) == 5 else (book[0], book[2] * book[3]), books))


if __name__ == "__main__":
    source_file = Path(__file__).with_name("books.csv")
    books = get_books(source_file)
    python_books = filtered_books(books, "python")
    print("Книги с python в названии:")
    print(python_books)
    print("Стоимость остатков по ISBN:")
    print(books_value(books[1:]))
