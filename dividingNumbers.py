inputNum = int(input("Please input a number: "))

if inputNum % 4 == 0:
    print(inputNum, " is divisible by 4.")
elif inputNum % 2 == 0:
    print(inputNum, " is even.")
else:
    print(inputNum, " is odd.")