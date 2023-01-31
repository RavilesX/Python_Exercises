import math
import os
import random
import re
import sys

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
