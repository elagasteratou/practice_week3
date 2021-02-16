supplied_pin = input("enter your pin")
correct_pin = '1234'
print(type(supplied_pin))
if supplied_pin == correct_pin:
    print("correct")
else:
    for i in range(0, 2):
        supplied_pin = input("enter your pin")
        print("incorrect")
# try a while loop and count the attempts