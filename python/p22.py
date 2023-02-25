#Exception handeling

a = input("Enter Number : ")
print(f"Multiplication table of {a} is : ")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print(e)
    print("Invalid INput")

print("Some imp lines of code")
print("End of code")

# try:
#     num = int(input("Please Enter Number  : "))
#     a = [6,3]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer")
# except IndexError:
#     print("Index Error")