import time
a=time.strftime('%H:%M:%S')
print(a)
hour=int (time.strftime('%H'))
if hour < 12:
    print("Good morning Sir")
elif hour>=12 and hour <=4:
    print("Good Afternoon Sir")
else:
    print("Good Evening Sir")