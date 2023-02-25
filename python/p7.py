#If Else elif
import time

'''applePrice = 20000
budget = int(input("Enter Your budget : "))

if(budget < applePrice):
    print("Budget is Low for Phone : ")
else:
    print("You are able to buy phone")'''

timestamp = time.strftime('%H:%M:%S')
hourshand = int(time.strftime('%H'))
minuteshand = int(time.strftime('%M'))
secondshand = int(time.strftime('%S'))
print(timestamp)

# 06:00:00 to 11:59:59 - Morning
# 12:00:00 to 16:59:59 - Afternoon
# 17:00:00 to 21:59:59 - Evening
# 22:00:00 to 05:59:59 - Night

if 5==hourshand or hourshand<=11 and minuteshand<=59 and secondshand<=59:
  print("Good Morning Sir !")
elif 12==hourshand or hourshand<=16 and minuteshand<=59 and secondshand<=59:
  print("Good Afternoon Sir !")
elif 17==hourshand or hourshand<=21 and minuteshand<=59 and secondshand<=59:
  print("Good Evening Sir !")
else:
  print("Good Night Sir !")