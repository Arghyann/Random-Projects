import random
ceil=10

A=[]
for i in range(0,ceil):
    A.append(random.randint(1,ceil))

def partFinder(arr,low,high):
    index=low-1
    if (high>low):
        partition=arr[high]
        for i in range(low,high):
            if(arr[i]<partition):
                index+=1
                arr[index],arr[i]=arr[i],arr[index]
        arr[index+1],arr[high]=arr[high],arr[index+1]        
        return index+1        
    return None    
            
def Quicksort(arr,low,high):
    if low<high:
        PartIndex=partFinder(arr,low,high)
        print(arr)
        Quicksort(arr,low,PartIndex-1)
        Quicksort(arr,PartIndex+1,high)
print("original array: ", A)
Quicksort(A,0,ceil-1)

