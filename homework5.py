immutable_var = 1, "Hello", True, 2.34
print(immutable_var)
# immutable_var[0] = False
# данная строка не может быть выполнена
# так как переменная immutable_var является кортежем
# кортеж нельзя изменять, он чемто похож на константу
mutable_list = [5, "Мир", False, 6.78]
mutable_list[0] = True
print(mutable_list)