strings = ["Banana", "apple", "cherry", "Date"]
numbers = [5, 12, 8, 15, 3, 20]

sorted_strings = sorted(strings, key=lambda x: x.lower()) # Сортировка без учета регистра
filtered_numbers = list(filter(lambda x: x > 10, numbers))

print("Отсортированные строки:", sorted_strings)
print("Числа больше 10:", filtered_numbers)