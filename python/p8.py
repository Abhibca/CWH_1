#Switch Case
Month = int(input("Enter your month between January to July : "))

match Month:
    case 0:
        print("This is not start from 0")    
    case 1:
        print("Janary")
    case 2:
        print("Febuary")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("june")
    
    case _ if Month>=6:
        print("You have break the range")
    case _:
        print(Month)