# Instruções de controle
# if - elif - else

x = float(input("Value of x: "))
y = float(input("Value of y: "))

if x > y:
    print(x, "is greater than", y)
elif x < y:
    print(x, "is less than", y)
else:
    print(x, "is equal to", y)