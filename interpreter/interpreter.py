#for expression
expression = input("expression ")
x, y, z = expression.split(" ")

#changing variable type
x = float(x)
z = float(z)

#for operator
match y:
    case "+":
        answer = (x + z)
    case "-":
        answer = (x - z)
    case "*":
        answer = (x * z)
    case"/":
        answer = (x / z)
print(round(answer, 1))




