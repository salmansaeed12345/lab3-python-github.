consent=str(input("do you want to proceed with calculations(yes/ no):"))

while (consent=="yes"):
    a = int(input("give your first number: "))
    b = int(input("give your 2nd number: "))


    def add(a, b):
     return a + b

    def mul(a, b):
     return a * b

    def dif(a, b):
     return a - b

    def div(a, b):
     if b == 0:
        return "cannot divide by zero"
     return a / b

    def per(a, b):
     if b == 0:
        return "cannot calculate percentage when 2nd number is zero"
     return a * 100 / b

    def ev_od(a, b):
     for n in (a, b):
        if n % 2 == 0:
            print(n," is even.")
        else:
            print(n," is odd.")

    print("the sum of numbers:", add(a, b))
    print("the difference of numbers:", dif(a, b))
    print("the division of numbers:", div(a, b))
    print("the multiplication of numbers:", mul(a, b))

    ask_ev_odd = input("want me to check if each number is even or odd? (yes/no): ").lower()

    if ask_ev_odd == "yes":
        ev_od(a, b)
    elif ask_ev_odd == "no":
        print("okay, not checking even/odd")
    else:
        print("wrong input")

    ask_perc = input("want me to find the percentage? (yes/no): ").lower()

    if ask_perc == "yes":
        print("the percentage of ",a,"with respect to",b," is:", per(a, b), "%")
    elif ask_perc == "no":
        print("okay, not giving you the percentage")
    else:
        print("wrong input")

    consent=str(input("do you want to continue with calculation or exit(yes/exit):"))