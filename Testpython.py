price = 0
discount = 10
number_of_tickets = input("Введите количество билетов: ")
for i in range(int(number_of_tickets)):
    age = input("Введите возраст: ")
    if int(age) < 18:
        price += 0
    elif 18 <= int(age) < 25:
        price += 990
    elif int(age) >= 25:
        price += 1390
print("Итоговая стоимость билетов (без учета скидки): ", price,"руб")
if int(number_of_tickets) > 3:
    price = price - (price * discount / 100)
print("общая стоимость покупки: ", price,"руб")
