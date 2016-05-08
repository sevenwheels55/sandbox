# get a list of divisors for a given number
def divisors(a):
    div = []
    for i in range (1, a + 1):
        if a % i == 0:
            div.append(i)
    return div

# get user input
num = int(input("Input a number: "))
print(divisors(num))
if len(divisors(num)) > 2:
    print(num, "is not a prime number.")
else:
    print(num, "is a prime number!")
