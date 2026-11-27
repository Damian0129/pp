money = 0
final_money = 0
percent = 0
current_year = 0

money = float(input("Введите сумму денег, которую вы кладёте в банк: "))

final_money = float(input("Введите сумму денег, к который вы хотите придти: "))

percent =int(input("Введите процент, который вам назначил банк: " ))

while money < final_money:
    current_year += 1

    money = money + money * percent / 100

    print(f"Прошёл {current_year} год. Сумма на счёт = {money:.2f}")

print(f"Чтобы на счету получить {money:.2f} Вам понадобиться {current_year} лет")
