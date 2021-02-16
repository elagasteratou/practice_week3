import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']
    print("home: ",hdir)
# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')
print("pattern", pattern)
# TODO: Use the glob.glob() function to obtain the list of filenames
list_files = glob.glob(pattern)
# print(list_files)
# TODO: use os.path.getsize to find each file's size
# for i in list_files:
#     size_of_file = os.path.getsize(i)
#     print(size_of_file)

# TODO: Add a test to only display files that are not zero length
# for i in list_files:
#     size_of_file = os.path.getsize(i)
#     if size_of_file != 0:
#         print(i, size_of_file)

# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()
print("original",list_files[0] )
print("basename for pattern", os.path.basename(list_files[0]))


