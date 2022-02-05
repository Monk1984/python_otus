
def print_two(*args):
    arg1, arg2 = args
    print('arg1: %r , arg2: %r' % (arg1, arg2))


def print_two_again(arg1, arg2):
    print("arg1: %s , arg2: %s" % (arg1, arg2))


def print_one(arg1):
    print("arg1: %s" % arg1)


def print_none():
    print("А я ничего не получаю.")


print_two("ionov", "aleksey")
print_two_again("ionov", "aleksey")
print_one("One")
print_none()


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(" У нас есть %d бутылок лимонада" % cheese_count)
    print(" У нас есть %d коробок чипсов" % boxes_of_crackers)
    print("Этого достаточно для вечеринки!")
    print("Поехали!!!")


print("Непосредственная передача:")
cheese_and_crackers(10, 30)


print("Значения из нашего сценария")
cheese = 30
crackers = 50
cheese_and_crackers(cheese, crackers)


print("Вычисления внутри функции")
cheese_and_crackers(10+15, 20+5)


print("Объединение")
cheese_and_crackers(cheese+100, crackers+150)

