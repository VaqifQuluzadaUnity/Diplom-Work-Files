import time
import mypy
from typing import List

def bubblesortFunction(mylist: List[int]):
    for iter_num in range(len(mylist)-1,0,-1):
        for idx in range(iter_num):
            if mylist[idx]>mylist[idx+1]:
                temp = mylist[idx]
                mylist[idx] = mylist[idx+1]
                mylist[idx+1] = temp

execution_start_time : float = time.time()

example_list: List[int] = [8,6,11,14,9,12,5]
bubblesortFunction(example_list)
print(example_list)

execution_end_time : float= time.time()

total_execution_time :float= execution_end_time -execution_start_time

print(total_execution_time)
