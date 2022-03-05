#Дурацкий калькулятор

znack = input("Какое действие(+,-,/,*)?: ")
a = float(input("Первое число: "))
b = float(input("Второе число: "))

if znack == "+":
    c = a + b
elif znack == "-":
    c = a - b
elif znack == "/":
    c = a / b
elif znack == "*":
    c = a * b
else:
    print("Неправильное действие")


print(c)

