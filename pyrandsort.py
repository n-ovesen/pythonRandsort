import re, string, sys, random, time
from random import randrange
sys.setrecursionlimit(10000)

size = int(sys.argv[1])     #system argument declaring size of array to sort
rng = int(sys.argv[2])      #system argument declaring range of numbers to sort

numbers = [random.randrange(rng) for x in range(size)]

def randomize(r):

	ret = random.randrange(r)			
	return ret;

def bsort(nums):

	end=len(nums) -1
	while (end != -1):
		swapped= -1

		for i in range(0,end):
			if nums[i]>nums[i+1]:
				temp = nums[i]
				nums[i] = nums[i+1]
				nums[i+1] = temp
				swapped = i
			end=swapped
	return nums

def quickSort(nums):
    less = []
    pivotList = []
    more = []
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums[0]
        for i in nums:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more

class Timer:    
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start


print "making array of ", size, " elements:\n\n"

#print "before sorting:", (numbers)

'''with Timer() as t:
    bsort(numbers)

print "bubblesort used:", t.interval*1000 , "milisecondsseconds to sort the array"'''

with Timer() as t:
	quickSort(numbers)

print "quicksort used:", t.interval*1000 , "milisecondsseconds to sort the array"