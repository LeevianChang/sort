# -*- coding: utf-8 -*-

def QuickSort(values,start,end):
    i = start
    j = end
    temp = values[start]
    if i==j:
        return values

    while i<j:
        while i<j:
            if values[j]>temp:
                values[i] = values[j]
                i = i+1
                break
            j = j-1
        while  i<j:
            if values[i]<temp:
                values[j] = values[i]
                j = j-1
                break
            i = i+1
    values[i] = temp
    if i>0:
        
        QuickSort(values,0,i)
    if i+1<end:
        
        QuickSort(values,i+1,end)

    return values

a = [1,4,5,7,8,0,3,1,15,6,89,334]
print(QuickSort(a,0,len(a)-1))
