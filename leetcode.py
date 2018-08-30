import sys
def merge(a, b):
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else: 
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c

def mergesort(x):
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = int(len(x)/2)
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])
        return merge(a, b)
       
   
if __name__ == '__main__':  
    nums = [10,8,4,-1,2,6,7,3]   
    mergesort(nums)  
    print ('merge sort:', mergesort(nums))
    
    


def insert_sort(a):  
    ''''' 插入排序 
    有一个已经有序的数据序列，要求在这个已经排好的数据序列中插入一个数， 
    但要求插入后此数据序列仍然有序。刚开始 一个元素显然有序，然后插入一 
    个元素到适当位置，然后再插入第三个元素，依次类推 
    '''  
    for i in range(1, len(a)):
        v = a[i]
        position = i
    
        while position > 0 and a[position-1] > v:
            a[position] = a[position-1]
            position = position -1
    
        a[position] = v
    
   
if __name__ == '__main__':  
    nums = [10,8,4,-1,2,6,7,3]  
    print ('nums is:', nums)  
    insert_sort(nums)  
    print (nums)
    
    
def select_sort(a):
    ''''' 选择排序  
    每一趟从待排序的数据元素中选出最小（或最大）的一个元素， 
    顺序放在已排好序的数列的最后，直到全部待排序的数据元素排完。 
    选择排序是不稳定的排序方法。 
    '''  
    a_len = len(a)
    for i in range(a_len):
        min_index = i
        for j in range(i+1, a_len):
            if(a[j] < a[min_index]):
              min_index = j
        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]
      
if __name__ == '__main__':  
    A = [10, -3, 5, 7, 1, 3, 7]    
    print ('Before sort:', A)   
    select_sort(A)    
    print ('After sort:',A)         

'''
快速排序            
 划分 使满足 以A[r]为基准对数组进行一个划分，比A[r]小的放在左边， 
   比A[r]大的放在右边 
快速排序的分治partition过程有两种方法， 
一种是上面所述的两个指针索引一前一后逐步向后扫描的方法, 
另一种方法是两个指针从首位向中间扫描的方法。   
'''

def partition(A, p, r):
    pivotvalue = A[p]   
    
    left = p+1
    right = r
    done = False
    while not done:
        while left <= right and A[left]<= pivotvalue:
              left = left + 1
        while A[right] >= pivotvalue and right >= left:
              right = right - 1
              
        if right < left:
            done = True
        else: 
            temp = A[left]
            A[left] = A[right]
            A[right] = temp
            
    temp = A[p]
    A[p] = A[right]
    A[right] = temp
    
    return right

def quickSort(A, p, r):
    if p < r:
        splitpoint = partition(A, p, r)
        quickSort(A, p, splitpoint -1)
        quickSort(A, splitpoint+1, r)
    
if __name__ == '__main__':  
   
    A = [5,-4,6,3,7,11,1,2]  
    quickSort(A, 0, 7)  
    print ('After sort:',A)


def bubbleSort(A):
    for p in range(len(A) -1, 0, -1):
        for i in range(p):
            if A[i] > A[i+1]:
                temp = A[i]
                A[i] =A[i+1]
                A[i+1] = temp
A = [54,26,93,17,77,31,44,55,20]
bubbleSort(A)
print(A)    
                
    
    