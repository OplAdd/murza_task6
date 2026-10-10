try:
    age = int(input())
    if age < 0 or age > 120:
        raise ValueError("Возраст вне допустимого диапазона")
except ValueError as e:
    print("Отклонено:", e)
else:
    print("Принято:", age)