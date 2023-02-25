#Custome error raising

a = input("Enter Value quiz : ")

try:
    if "quiz" in a:
        print("you have entered right string")
    else:
        raise Exception("This is not quiz")

except Exception as error:
    print('Caught this error: ' + repr(error))

