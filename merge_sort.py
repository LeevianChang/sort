



def MergeSort(values,i,j):
    # print(i,j)
    if i == j:
        return 
    
    mid = int((i+j)/2)
    MergeSort(values,i,mid)
    MergeSort(values,mid+1,j)
    Merge(values,i,mid,j)


def Merge(values,i,mid,j):
    v = []
    p1 = i
    p2 = mid+1
    while p1 <=mid and p2<=j:
        if values[p1]<values[p2]:
            v.append(values[p2])
            p2 = p2+1
        else:
            v.append(values[p1])
            p1 = p1+1
  
    while p1<=mid:
        v.append(values[p1])
        p1 = p1+1
        

    while p2<=j:
        v.append(values[p2])
        p2 = p2+1
            
    print(v)
        
    for index in range(len(v)):
        values[i+index] = v[index]




a = [1,3,543,647,21,3,2,234,45,51]

MergeSort(a,0,len(a)-1)
print(a)