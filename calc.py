import math
print ("welcome to the mehthematical calc (short for calculator)")
def addition(x, y):
    return x + y
def subtraction(x, y):
    return x - y
def multiplication(x, y):
    return x * y
def division(x, y):
    if y == 0:
        return False
    else:
        return x / y
def exponent(x, y):
    return pow(x, y)
def real_number_calculator(num):
    try:
        super_num = float(num)
    except ValueError:
        print("wow, thats not a number, you cant do anything right")
        return False
    else:
        return True
super_working = False
while True == True:
    while True == True:
        print ("what operation do you want, please pick a easy one")
        the_ops_tryna_swiss_cheese_me = input(" 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Exponent \n ")
        if the_ops_tryna_swiss_cheese_me == "1" or the_ops_tryna_swiss_cheese_me == "2" or the_ops_tryna_swiss_cheese_me == "3" or the_ops_tryna_swiss_cheese_me == "4" or the_ops_tryna_swiss_cheese_me == "5":
            break
        else:
            print ("how hard could it be to type a number")
    while True == True:
        x = input ("what should the first number be? \n ")
        super_working = real_number_calculator(x)
        if super_working == True:
            x = float(x)
            break
        else:
            print ("make my job easy, give me a real number")    
    while True == True:
        y = input ("i guess i need a second number too \n ")
        super_working = real_number_calculator(y)
        if super_working == True:
            y = float(y)
            break
        else:
            print ("make my job easy, give me a real number")
    if the_ops_tryna_swiss_cheese_me == "1":
        result = addition(x, y)
        print (f"your number is {result}")
    elif the_ops_tryna_swiss_cheese_me == "2":
        result = subtraction(x, y)
        print (f"your number is {result}")
    elif the_ops_tryna_swiss_cheese_me == "3":
        result = multiplication(x, y)
        print (f"your number is {result}")
    elif the_ops_tryna_swiss_cheese_me == "4":
        result = division(x, y)
        if result == False:
            print ("you cant divide by 0, you really cant do anything right")
        else:
            print (f"your number is {result}")
    elif the_ops_tryna_swiss_cheese_me == "5":
        result = exponent(x, y)
        print (f"your number is {result}")
    print ("please say you dont want to do more math")
    while True == True:
        again = input (" 1. Do another calculation \n 2. Exit \n ")
        if again == "2":
            print ("screw off then")
            exit()
        elif again == "1":
            break
        else:
            print ("i'm just gonna pretend you said 2")
            exit()