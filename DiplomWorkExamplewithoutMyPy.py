import time

def bubblesortFunction(mylist):
    for iter_num in range(len(mylist)-1,0,-1):
        for idx in range(iter_num):
            if mylist[idx]>mylist[idx+1]:
                temp = mylist[idx]
                mylist[idx] = mylist[idx+1]
                mylist[idx+1] = temp

execution_start_time = time.time()

example_list = [8,6,11,14,9,12,5]
bubblesortFunction(example_list)
print(example_list)

execution_end_time= time.time()

total_execution_time= execution_end_time -execution_start_time

print(total_execution_time)

