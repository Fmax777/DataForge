print("Подсчёт и суммирование чётных чисел")
num = int(input("Введите число: "))
total = 0
count = 0

for number in range(1, num + 1):
    if number % 2 == 0:
        total += number
        count += 1

print(f"Сумма четных чисел: {total}")
print(f"Количество четных чисел: {count}")