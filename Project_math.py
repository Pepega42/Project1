import math
while True:
    calc = input("+, -, /, **, sqrt, !, sin, cos, tg: ")    
    if calc == "+":
        try:
            numb1 = float(input("Введите первое число: "))
            numb2 = float(input("Введите второе число: "))
            print(numb1 + numb2)
        except:
            print("Данное число не сработает")
    elif calc == "-":
        try:    
            numb1 = float(input("Введите первое число: "))
            numb2 = float(input("Введите второе число: "))
            print(numb1 - numb2)
        except:
            print("Данное число не сработает")
    elif calc == "*":
        try:    
            numb1 = float(input("Введите первое число: "))
            numb2 = float(input("Введите второе число: "))
            print(numb1 * numb2)
        except:
            print("Данное число не сработает")
    elif calc == "/":
        try:    
            numb1 = float(input("Введите первое число: "))
            numb2 = float(input("Введите второе число: "))
            if:
                numb2 != 0
            print(numb1 / numb2)
        except:
            print("Данное число не сработает")
    elif calc == "**":
        try:    
            numb1 = float(input("Введите первое число: "))
            numb2 = float(input("Введите второе число: "))
            print(numb1 ** numb2)
        except:
            print("Данное число не сработает")
    elif calc == "**":
        try:    
            numb1 = float(input("Введите первое число: "))
            print(math.sqrt(numb1))
        except:
            print("Данное число не сработает")
    elif calc == "!":
        try:    
            numb1 = float(input("Введите первое число: "))
            print(math.factorial(numb1))
        except:
            print("Данное число не сработает")
    elif calc == "sin":
        try:    
            numb1 = float(input("Введите первое число: "))
            numb1 = math.radians(numb1)
            print(math.sin(numb1))
        except:
            print("Данное число не сработает")
    elif calc == "cos":
        try:    
            numb1 = float(input("Введите первое число: "))
            numb1 = math.radians(numb1)
            print(math.cos(numb1))
        except:
            print("Данное число не сработает")
    elif calc == "tg":
        try:    
            numb1 = float(input("Введите первое число: "))
            numb1 = math.radians(numb1)
            print(math.tan(numb1))
        except:
            print("Данное число не сработает")
    else:
        print("Такой операции нет")
