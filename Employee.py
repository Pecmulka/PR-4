class Employee:
    def __init__(self, name, salary):
        self.__name = name
        if salary < 0:
            raise ValueError("Зарплата не может быть отрицательной")
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def raise_salary(self, amount):
        if amount < 0:
            raise ValueError("Сумма повышения не может быть отрицательной")
        self.__salary += amount

    def get_name(self):
        return self.__name

try:
    emp = Employee("Иван Иванов", 50000)
    print(f"{emp.get_name()}, текущая зарплата: {emp.get_salary()}")

    emp.raise_salary(10000)
    print(f"Зарплата {emp.get_name()} после повышения: {emp.get_salary()}")

    # Попытка установить отрицательную зарплату при создании
    emp2 = Employee("Петр Петров", -1000)  # Вызовет ValueError: Зарплата не может быть отрицательной

    # Попытка повысить зарплату на отрицательную сумму
    # emp.raise_salary(-5000)  # Вызовет ValueError: Сумма повышения не может быть отрицательной

except ValueError as e:
    print(f"Ошибка: {e}")