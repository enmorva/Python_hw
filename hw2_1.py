print("Сколько элементов?")
n = int(input())
l = []
for i in range(n):
    print("Введите элементы")
    x = input()
    l.append(x)
print("Введите степень")
st = int(input())
rezult = []
for el in l:
    rezult.append(int(el) ** st)
print("Итого:", rezult)
