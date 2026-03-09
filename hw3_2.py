import math

def plus(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Оба аргумента должны быть числами")
    return a + b

def minus(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Оба аргумента должны быть числами")
    return a - b

def umnozenie(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Оба аргумента должны быть числами")
    return a * b

def delenie(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Оба аргумента должны быть числами")
    if b == 0:
        raise ZeroDivisionError("На ноль делить нельзя")
    return a / b

def stepen(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Оба аргумента должны быть числами")
    return a ** b

def faktorial(n):
    if not isinstance(n, int):
        raise TypeError("Факториал только для целых чисел")
    if n < 0:
        raise ValueError("Факториал отрицательного числа не существует")
    if n == 0:
        return 1
    res = 1
    for i in range(1, n + 1):
        res = res * i
    return res

def sinus(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Аргумент должен быть числом")
    return math.sin(x)

def ostatok(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Оба аргумента должны быть числами")
    if b == 0:
        raise ZeroDivisionError("На ноль делить нельзя")
    return a % b

print("Доступные операции:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Возведение в степень")
print("6. Факториал")
print("7. Синус")
print("8. Остаток от деления")

while True:
    oper = input("\nОперация: ")
    
    if oper == "exit":
        print("exit")
        break
    
    try:
        if oper == "1":
            a = float(input("Число 1: "))
            b = float(input("Число 2: "))
            print(f">>> {plus(a, b)}")
            
        elif oper == "2":
            a = float(input("Число 1: "))
            b = float(input("Число 2: "))
            print(f">>> {minus(a, b)}")
            
        elif oper == "3":
            a = float(input("Число 1: "))
            b = float(input("Число 2: "))
            print(f">>> {umnozenie(a, b)}")
            
        elif oper == "4":
            a = float(input("Число 1: "))
            b = float(input("Число 2: "))
            print(f">>> {delenie(a, b)}")
            
        elif oper == "5":
            a = float(input("Число: "))
            b = float(input("Степень: "))
            print(f">>> {stepen(a, b)}")
            
        elif oper == "6":
            n = int(input("Число: "))
            print(f">>> {faktorial(n)}")
            
        elif oper == "7":
            x = float(input("Число: "))
            print(f">>> {sinus(x)}")
            
        elif oper == "8":
            a = float(input("Число 1: "))
            b = float(input("Число 2: "))
            print(f">>> {ostatok(a, b)}")
            
        else:
            print("Неизвестная операция")
            
    except ZeroDivisionError as e:
        print(f"Ошибка: {e}")
    except TypeError as e:
        print(f"Ошибка типа: {e}")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")
