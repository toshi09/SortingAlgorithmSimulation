# -*- coding: utf-8 -*-
"""

"""
import random
# Time requred to compare the time of execution
import time 
# numpy to generate the random function
import numpy 
# python memory profiler
from memory_profiler import profile
from scipy import stats

def compare(a,b):
    """
    Compare two numbers
    """
    if a<b: return (-1)
    if a>b: return( 1)
    return( 0)

def distribute(bins,L,fn):
    """
    helper routine for quick sort.
    """
    for item in L:
        bins[fn(item)].append(item)
@profile
def qsort(L):
    """
    QuickSort algorithm
    """
    if len(L)<2: return L
    pivot_element = random.choice(L)
    bins = {-1:[],0:[],1:[]}
    distribute(bins,L, lambda item : compare(item, pivot_element) )
    return qsort(bins[-1])+bins[0]+qsort(bins[1])

def merge(left, right):
    """
    Merge two sorted lists.
    Used by merge_sort algorithm.
    """
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
 
    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result

@profile
def merge_sort(m):
    """
    Merge Sort Algorithm
    """
    if len(m) <= 1:
        return m
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]
 
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

@profile
def bubble_sort(alist):
    """
    Bubble Sort algorithm
    """
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist

@profile
def insertion_sort(alist):
   """
   Insertion sort
   """
   for index in range(1,len(alist)):
       currentvalue = alist[index]
       position = index
       while position>0 and alist[position-1]>currentvalue:
           alist[position]=alist[position-1]
           position = position-1
   alist[position]=currentvalue
   return alist
   
@profile   
def selection_sort(alist):
   """
   Selection sort
   """
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp
   return alist 


def degree_randomness(list_of_numbers):
     """
     Degree of randomness using measure of entroy.
     """
     return stats.entropy(list_of_numbers)

def avg_execution_time(func, list_of_numbers):
   """
   Calcuate the average execution time of function from
   five runs.
   """
   times = []
   for i in range(0,5):
       start = time.time()
       func(list_of_numbers)
       total_time =  time.time() - start
       times += [total_time]
   return sum(times) / 5.0  

data_set_1 =  list(numpy.random.random_integers(1,10000,10000))   
data_set_2 =  list(numpy.random.random_integers(1,20000, 20000))
house_hold_data= [ int(line.strip()) for line in open("/Users/vikhyati/Downloads/block_no_of_house_holds.csv")]           
illiterate_data= [ int(line.strip(",\n")) for line in open("/Users/vikhyati/Downloads/Total_illiterate.csv")]           

def exection_time_by_data_set_size(list_num):
    """
    Print the execution time for five sorting algorithms
    for the list of numbers
    """
    print(avg_execution_time(merge_sort, list_num[:]))
    print(avg_execution_time(qsort, list_num[:]))
    print(avg_execution_time(bubble_sort, list_num[:]))
    print(avg_execution_time(insertion_sort, list_num[:]))
    print(avg_execution_time(selection_sort, list_num[:]))
"""
Following is the example of print execution time of the
five sorting algorithms for data_set_1 and data_set_2.
We get the execution time for each of the datasets by calling
them in python interpreter one by one.
"""
#exection_time_by_data_set_size(data_set_1)
#exection_time_by_data_set_size(data_set_2)

def print_degree_of_randomness():
    """
    Print the degree of randomness for the four datasets
    """
    print(degree_randomness(data_set_1))
    print(degree_randomness(data_set_2))
    print(degree_randomness(house_hold_data))
    print(degree_randomness(illiterate_data))

# We create yet another two large dataset to measure memory.
data_set_large =  list(numpy.random.random_integers(1,1000000,1000000))   
data_set_x_large =  list(numpy.random.random_integers(1,2000000, 2000000))

@profile
def measure_memory(func, list_num):
    """
    Measure memory of function though mprof utility.
    Notice I have used @profile decorator.
    This is a wrapper function to measure memory
    """
    val = func(list_num)
    return val
    
"""
Following is the example of memory profiling the merge_sort function
for the data_set_large.
We do this profiling for each of the sorting functions one be one
for each of the datasets on the standard python interpreter shell.
"""
#measure_memory(merge_sort, data_set_large[:])  
#measure_memory(bubble_sort, house_hold_data[:])  
#measure_memory(merge_sort, illiterate_data[:])  

# data_set_large merge_sort 135MB
# data_set_large qsort 154MB
# data_set_large bubble_osrt 118MB
# data_set_large insertion_sort 118MB
# data_set_large selection_sort 118MB


# data_set_x_large merge_sort 160MB
# data_set_x_large qsort 169MB
# data_set_x_large bubble_sort 125MB
# data_set_x_large insertion_sort 125MB
# data_set_x_large selection_sort 125MB


merge_sort(house_hold_data[:])


