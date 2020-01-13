for number in range(1, 101):
    if number % 7 == 0 and number % 5 == 0:
        print(f"{number} ChickenMonkey")
    elif number % 7 == 0:
        print(f"{number} Monkey")
    elif number % 5 == 0:
        print(f"{number} Chicken")
    else:
        print(number)
