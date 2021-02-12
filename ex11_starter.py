#!/usr/bin/python
from typing import List

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
# new_str = ""
# for i in Belgium:
#     new_str += "-"
# print(new_str)
# print(len(Belgium), len(new_str))

split_Belgium: list[str] = Belgium.split(",")
print(split_Belgium)
join_Belgium = ": ".join(split_Belgium)
print(join_Belgium, "\n addition is equal to ", (int(split_Belgium[1]) + int(split_Belgium[3])))