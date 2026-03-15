def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Функция `{func.__name__}` вызвана с аргументами:")
        print(f"Позиционные аргументы: {args}")
        print(f"Именованные аргументы: {kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@decorator
def rectangle(width, height):
    return width * height

result = rectangle(5, 10)
print(f"Площадь прямоугольника: {result}")
