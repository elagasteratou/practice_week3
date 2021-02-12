import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')

# TODO: Use the glob.glob() function to obtain the list of filenames

# TODO: use os.path.getsize to find each file's size

# TODO: Add a test to only display files that are not zero length

# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()

supplied_pin = input("enter your pin")
correct_pin = '1234'
print(type(supplied_pin))
if supplied_pin == correct_pin:
    print("correct")
else:
    for i in range(0, 2):
        supplied_pin = input("enter your pin")
        print("incorrect")
