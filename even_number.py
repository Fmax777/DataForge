print("Суммирование, умножение и подсчёт чётных чисел")
num = int(input("Введите верхнюю границу диапазона: "))
total = 0
product = 1
count = 0

for number in range(1, num + 1):
    if number % 2 == 0:
        total += number
        product *=number
        count += 1

print(f"Сумма чётных чисел: {total}")
print(f"Произведение чётных чисел: {product}")
print(f"Количество чётных чисел: {count}")