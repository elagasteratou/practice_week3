# #####for loop exercises
# names = ["MG", "LA", "JW"]
#
# for j in names:
#     print(j, "hello")

# #####enumerate
# countries = ["Greece", "Ethiopia", "England"]
#
# for j, item in enumerate(countries):
#     print("index:", j, "item:", item)
#

# #####range

# my_colour = "blue"
#
# for i in range (0, 2):
#     index = my_colour[i]
#     print(index)

# #####string spliting and joining

# my_name = "Michaela,Gasteratou"
# split_name = my_name.split(",")  #will be a list
# print(split_name, "and is an", type(split_name))
#
# joined_names = " ".join(split_name)
#
# print(joined_names, "and is an", type(joined_names))

###### katas with loops 1

# def positive_sum(arr):
#     total = 0
#     for i in range (0, len(arr)):
#         if arr[i] >= 0:
#             total += arr[i]
#         else:
#             return 0
#
#     return total
# positive_sum([1,2,3])
# ###### katas with loops 2
# def repeat_str(repeat, string):
#     new = ""
#
#     for i in range(repeat):
#         new += string
#
#     return new
# repeat_str(4, "hello")
