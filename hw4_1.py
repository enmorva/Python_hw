from math import factorial

squares = [x**2 for x in range(1, 11)]
print("1.", squares)

days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
days_dict = {day: i+1 for i, day in enumerate(days)}
print("2.", days_dict)

tags = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
tags_set = {tag.lower() for tag in tags}
print("3.", tags_set)

numbers = [1, 3, 4, 87, 98, 15, 7, 4]
even_numbers = [num for num in numbers if num % 2 == 0]
print("4.", even_numbers)

factorials = {n: factorial(n) for n in range(1, 6)}
print("5.", factorials)
