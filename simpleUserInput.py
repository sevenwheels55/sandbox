something =  input("Enter some input: ")

try:
    print("The unadulterated input: ", something)
    print("As a boolean value: ", bool(something))
    print("As an integer: ", int(something))

    print("As a float: ", float(something))


except:
    print("There was an error")