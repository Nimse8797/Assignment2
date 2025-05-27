
def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    elif n<0:
        print("Factorial cannot be negative")
    else:
        return n*factorial(n-1)


n = int(input("Enter a number\t"))
print("The factorial of ",n,"is", factorial(n))