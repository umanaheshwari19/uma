import numpy as np

def add(a, b):
    return np.add(a, b)

def subtract(a, b):
    return np.subtract(a, b)

def multiply(a, b):
    return np.multiply(a, b)

def divide(a, b):
   if b!=0:
       return np.divide(a,b)
   else:
       return"Error! Division by zero."
def power(a,b):
    return np.power(a,b)


def calculator():
    print("Welcome to the  Calculator!")
while True:
    print("select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. power")
    print("6. exit")


    choice = input("Enter choice (1/2/3/4/5/6): ")
    if choice=='6':
        print("Exiting calculator...")
        break

    s1 = float(input("Enter the first number: "))
    s2 = float(input("Enter the second number: "))

        # Perform operation based on user choice
    if choice == '1':
            print(f"{s1} + {s2} = {add(s1, s2)}")
    elif choice == '2':
            print(f" {s1} - {s2} ={subtract(s1, s2)}")
    elif choice == '3':
            print(f" {s1} * {s2} = {multiply(s1, s2)}")
    elif choice == '4':
            print(f" {s1} / {s2} = {divide(s1, s2)}")
    elif choice == '5':
            print(f"{s1} ^ {s2} = {power(s1, s2)}")
    else:
        print("Invalid input! Please try again.")


    if __name__ == "__main__":
      calculator()