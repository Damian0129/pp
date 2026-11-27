money = 0
percent = 0
current_year = 0
final_year = 0
start_money = 0

money = float(input("Введите сумму денег, которую вы кладёте в банк: "))

percent = float(input("Введите процент, который вам назначил банк: "))

current_year = 0

final_year =int(input("Введите колличество лет,на которые вы кладёте сумму в банк: " ))

start_money = money

while current_year<final_year:
    current_year += 1

    money = money + money * percent / 100

    print(f"По прошествию {current_year} лет. Вы заработали = {money:.2f}")

profit = money - start_money
