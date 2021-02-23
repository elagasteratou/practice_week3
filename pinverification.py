supplied_pin = input("enter your pin")
correct_pin = '1234'
print(type(supplied_pin))
i = 0

if supplied_pin == correct_pin:
    print("correct")
else:
    while i<2:
        supplied_pin = input("enter your pin")
        print("incorrect")
        i+=1
# try a while loop and count the attempts