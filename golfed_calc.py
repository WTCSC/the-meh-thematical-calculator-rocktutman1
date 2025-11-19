def n(m):
    while 1:
        v=input(m)
        try: return float(v)
        except: print("error")
def add(x, y):return round(x + y,10)
def sub(x, y):return round(x - y,10)
def m(x, y):return round(x * y,10)
def div(x, y):
    if y == 0:
        return False
    else:
        return round(x / y,10)
def exponent(x, y):return round(pow(x, y),10)
d = 0
while 1:
    while 1:
        k = input("1.+\n2.-\n3.*\n4./\n5.**\n")
        if k in "12345":
            break
        else:
            print ("error")
    x = n("num1 ")
    y = n("num2 ")
    ops={"1":add,"2":sub,"3":m,"4":div,"5":exponent}
    i=ops[k](x,y)
    if i != False:
        print(i)
    else:
        print("error")
    r = input ("1. Do another ")
    if r!="1":exit()