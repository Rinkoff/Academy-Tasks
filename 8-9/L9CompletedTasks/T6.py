book_list = [
    ("Името на вятъра", "Патрик Ротфус", 2007),
    ("Гордост и предразсъдъци", "Джейн Остин", 1813),
    ("1984", "Джордж Оруел", 1949),
    ("Автостопом по галактиката", "Дъглас Адамс", 1979),
    ("Триумфът на бръмбарите", "Аркадий и Борис Стругацки", 1968),
    ("Война и мир", "Лев Толстой", 1869),
]

for book in book_list:
    if book[2] < 2000:
        print(book[0])