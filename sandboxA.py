palintest = False
phrase = input("Please input a word or phrase: ")
palindrome = phrase.replace(" ", "").lower()
length = len(palindrome)
midpoint = int(length / 2)
secondHalf = palindrome[midpoint:length]
if length % 2 == 0:
    firstHalf = palindrome[0:midpoint]
    backwards = midpoint - 1
else:
    firstHalf = palindrome[0:midpoint + 1]
    backwards = midpoint
# remember that the end number in a range in non inclusive

## print(firstHalf, secondHalf, midpoint)
for i in secondHalf:
    if i != firstHalf[backwards]:
        palintest = False
        break
    else:
        palintest = True
    backwards = backwards - 1

if palintest:
    print(phrase, "is a palindrome.")
else:
    print(phrase, "is not a palindrome.")