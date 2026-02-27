print("Введите строку:")
text = input()
w = text.lower().split()
result = {}
for wd in w: 
    count_wd = w.count(wd)
    result[wd] = count_wd
for wd in result:
    print(wd + ":", result[wd])
