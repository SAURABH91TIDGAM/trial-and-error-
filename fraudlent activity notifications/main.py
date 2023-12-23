#!/bin/python3

import math
import os
import random
import re
import sys
from bisect import bisect_left, insort_left


#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    first_day = count = 0
    last_day = d
    temp_arr = sorted(expenditure[:d])

    while last_day <= len(expenditure) - 1:
        temp = temp_arr[d // 2]
        median = temp if d % 2 != 0 else (temp_arr[(d // 2) - 1] + temp) / 2

        if median * 2 <= expenditure[last_day]:
            count += 1

        del temp_arr[bisect_left(temp_arr, expenditure[first_day])]
        first_day += 1
        last_day += 1
        insort_left(temp_arr, expenditure[last_day - 1])

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
