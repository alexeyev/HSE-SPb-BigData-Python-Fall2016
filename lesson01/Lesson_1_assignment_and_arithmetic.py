
"""
  Оператор присваивания и арифметика
"""

# задаём значения переменных
a = 2
b = 12
c = 85.0
d = -6

# записываем другое значение в a
# теперь под именем a скрывается не 2, а 5
a = 5
print(a == 5)

quit()

# записываем в b результат операции над какими-то двумя другими переменными
# меняется только значение переменной b
b = - d + c
print(b == 12)
print(b == c - d)
print(b==-d+c)

quit()

# записываем в c результат вычисления выражения с участием его прежнего значения
c = c + d

# c больше не равно 85, так как мы изменили значение
print(c == 85.0)

# что происходит, когда мы так делаем? 
# сначала мы вычислили правую часть: (с + d) = (85.0 + (-6)) = 79.0
# и так же, как в примере с a, просто записали это число в c, поэтому здесь
print(c == c + d)
# конечно, False: 79.0 не равно 79.0 + (-6)

quit()

# деление нацело

print(12 // 6)
print(-12 // 6)

quit()

# в питоне -- floor division, то есть при делении нацело мы округляем в меньшую сторону

print(-13 // 6)
print(-13 // 6)
print(12 // 5)

quit()

# остаток при делении -- он и есть остаток при делении

print(12 % 5)
print(7 % 2)

