#Fstring
letter = "Hello my name is {1} and I'm from {0}"
name = "Abhishek"
country = "India"

print(letter.format(country,name))
print(f"My name is {name} and I'm from {country}")
print(f"we use f string like this : hey my name is {{name}} and I'm from {{country}}")

price = 49.000
txt = f"for only{price:.2f} Dollors"
print(txt)

print(f"{30*2}")

#Doc string
def square(n):
    '''This function is usaly shows a square os any purticular number'''
    print(n**2)

square(5)
print(square.__doc__)