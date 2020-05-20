j = eval(input("Weka namba yoyote mzee:"))
try:
    a =   3/j
    print(a)

    if j <= 0:
        raise ZeroDivisionError("Usiweke sifuri mzee!")
except:
    print("zaga!")