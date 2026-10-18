# 1) Create a function to calculate the mean of a list:
#    a) Add all elements using a loop.
#    b) Mean = total sum / number of elements.
#    c) Return the mean as a float.

# 2) Create a function to calculate the median of a list:
#    a) Sort the list first.
#    b) If the size is odd, return the middle element.
#    c) If the size is even, return the average of the two middle elements.

# 3) Create a sample list and find its size using `len()`.

# 4) Call both functions and print the mean and median.

def mean (array,arraysize):
    total_sum = 0 
    for i in range(0,arraysize):
        total_sum += array[i]
    return float(total_sum/arraysize)
def median(array,arraysize):
    sorted(array)
    if arraysize%2!=0:
        return float(array[int(arraysize/2)])
    else:
        return float((array[int((arraysize-1)/2)]+array[int(arraysize/2)])/2)
array=[1,2,3,4,5,6,7]   
arraysize=len(array)
print("mean=",mean(array,arraysize))
print("median",median(array,arraysize))

def minelement(a,size):
    temp=a[0]
    for i in range(1,size):
        temp=min(temp,a[i])
    return temp
def maxelement(a,size):
    temp=a[0]
    for i in range(1,size):
        temp=max(temp,a[i])
    return temp
a = [2,0,1,4,2,2,5,3]
size=len(a)
print("minum of given element is",minelement(a,size))
print("max of given element is",maxelement(a,size))

def secondlargestnumber(a,size):
    largest=secondlargest=-2147483648
    for i in range(size):
        if a[i] > largest:
            secondlargest=largest
            largest=a[i]
        elif a[i] > secondlargest and a[i] !=largest:
             secondlargest=a[i]
    print(secondlargest)
a = [3,6,3,8,9,1]
size = len(a)
secondlargestnumber(a,size)