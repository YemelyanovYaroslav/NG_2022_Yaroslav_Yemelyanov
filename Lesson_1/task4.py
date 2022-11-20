quadratСoef = int(input("Enter the quadratic coefficient: "))
linearCoef = int(input("Enter the linear coefficient: "))
freeСonstant = int(input("Enter a free constant: "))

if quadratСoef != 0 and linearCoef != 0 and freeСonstant != 0:
    discriminant = linearCoef ** 2 - 4 * (quadratСoef * freeСonstant)
    x1 = (- linearCoef + discriminant ** 0.5) / (2 * quadratСoef)
    x2 = (- linearCoef - discriminant ** 0.5) / (2 * quadratСoef)
    print(f"x1 = {x1}\nx2 = {x2}")
    
if quadratСoef != 0 and linearCoef == 0 and freeСonstant != 0:
    if (- freeСonstant / quadratСoef) > 0:
        x1 = (- freeСonstant / quadratСoef) ** 0.5
        x2 = - (- freeСonstant / quadratСoef) ** 0.5
        print(f"x1 = {x1}\nx2 = {x2}")
    elif (- freeСonstant / quadratСoef) < 0:
        print("The equation has no solution")

if quadratСoef != 0 and linearCoef != 0 and freeСonstant == 0:
    x1 = 0
    x2 = - linearCoef / quadratСoef
    print(f"x1 = {x1}\nx2 = {x2}")

if quadratСoef != 0 and linearCoef == 0 and freeСonstant == 0:
    x = 0
    print(f"x = {x}")