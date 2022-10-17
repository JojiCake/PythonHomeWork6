s = 0
number = input('Введите число: ')
res = list(map(int, [chislo for chislo in number if chislo.isdigit()]))
for el in res:
    s += el
print(s)