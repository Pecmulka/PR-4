from datetime import datetime

class Book:
    def __init__(self, title, author, year):
            self.title = title
            self.author = author
            self.year = year

    def get_info(self):
        return f"{self.title} ({self.author}, {self.year})"

    def is_classic(self):
        return (datetime.now().year - self.year) > 50

# Создаем объект книги
book1 = Book("Война и мир", "Лев Толстой", 1869)

# Получаем информацию о книге
print(book1.get_info())  # Выведет: Война и мир (Лев Толстой, 1869)

# Проверяем, является ли книга классикой
print(book1.is_classic())  # Выведет: True (так как прошло больше 50 лет)

# Пример с более новой книгой
book2 = Book("Гарри Поттер", "Джоан Роулинг", 1997)
print(book2.is_classic())  # Выведет: False (если текущий год 2025)