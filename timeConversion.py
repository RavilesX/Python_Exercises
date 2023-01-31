import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#a
s="12:05:45AM"
def timeConversion(s):
    hours=int(s[0:2])
    if s.__contains__("PM"):
        if hours!=12:
            hours=hours+12
    else:
        if hours==12:
            hours=0    
    military=f"{str(hours).zfill(2)}"+s[2:8]
    return military

        
result = timeConversion(s)
print(result)
