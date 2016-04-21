# This algorithm is incomplete as it does not account for punctuation in the input.

palintest = False
phrase = input("Please input a word or phrase: ")
# Take the input and remove whitespaces and reduces all letters to lowercase.
palindrome = phrase.replace(" ", "").lower()
length = len(palindrome)
midpoint = int(length / 2)
secondHalf = palindrome[midpoint:length]
# Check if the number of characters is odd or even then include the
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