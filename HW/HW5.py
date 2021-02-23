first_c = int(input("Введите кол-во учеников в 1м классе:"))
second_c = int(input("Введите кол-во учеников в 2м классе:"))
third_c = int(input("Введите кол-во учеников в 3м классе:"))

desk_one = first_c % 2 + first_c // 2
desk_two = second_c % 2 + second_c // 2
desk_three = third_c % 2 + third_c // 2

print("Необходимо купить {0} парт и {1} стульев в первый класс".format(desk_one, first_c))
print("Необходимо купить {0} парт и {1} стульев во второй класс".format(desk_two, second_c))
print("Необходимо купить {0} парт и {1} стульев в третий класс".format(desk_three, third_c))

