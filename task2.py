'''Задача 2: Найдите сумму цифр трехзначного числа.'''
chislo = int(input())
x1 = int(chislo / 100)
x2 = int((chislo % 100) / 10)
x3 = int(chislo % 10)
#print(x1 , x2 , x3)
summa = x1+ x2 + x3
print(chislo , "->", summa, "(",x1,"+",x2,"+",x3,")")