import math

while True:
    calculationchoice = input("A(rea) or N(umber) or P(ythagoras) or Q(uit): ").upper()

    if calculationchoice == "N":
        num1 = int(input("Choose a number: "))
        num2 = int(input("Choose another number: "))
        op = input("Choose an operator (+, -, *, /, ^): ")
        display_op = op

        if op not in "*/+-^":
            print("Invalid operator!!")
        else:
            if op == "^":
                op = "**"
            print(f"{num1} {display_op} {num2} is equal to {eval(f'{num1}{op}{num2}')}")

    elif calculationchoice == "A":

        def area(width, height):
            return width * height

        sh = input("Choose a shape (Circle, Square, Triangle): ").lower()
        if sh == "circle":
            r = int(input("Enter the radius of your circle: "))
            print(f"The area of your circle is equal to {eval(f'{math.pi}*{r}**2')}")
        elif sh == "triangle":
            w = int(input("Enter the base of your triangle: "))
            h = int(input("Enter the height of your triangle: "))
            print(f"The area of your triangle is equal to {area(w, h) / 2}")
        elif sh == "square":
            w = int(input("Enter the width of your square: "))
            h = int(input("Enter the height of your square: "))
            print(f"The area of your square is equal to {area(w, h)}")
        else:
            print("Invalid shape!")

    elif calculationchoice == "P":
        a = int(input("Enter side A: "))
        b = int(input("Enter side B: "))
        csqr = f"({a}**2)+({b}**2)"
        print(f"{a}^2 + {b}^2 is equal to {eval(csqr)} (C^2), {eval(f'{math.sqrt((a**2)+(b**2))}')} (C)")

    elif calculationchoice == "Q":
        quit("ok bye bye")

    else:
        print("Invalid choice!")
