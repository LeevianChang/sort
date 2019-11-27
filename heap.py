#-*-coding:utf-8-*-


def swap(values,a,b):
	temp = values[a]
	values[a] = values[b]
	values[b] = temp

def heapify(values,n,i):
	left_node =(2*i)+1
	right_node = (2*i)+2
	max = i
	if left_node<n and  values[left_node]>values[max]:
		max =left_node
	if right_node<n and  values[right_node]>values[max]:
		max = right_node
	if i!=max:
		swap(values,i,max)
		heapify(values,n,max)

def build_heap(values,n):
	parent = int((n-1)/2)
	
	for i in range(parent,-1,-1):
		heapify(values,n,i)
	return values


a = [1,4,5,8,9,11,2,1,3,67,2,2,2,3,7,6,1,0]
print(build_heap(a,len(a)))


def sort(values):
	n = len(values)-1
	for i in range(len(values)-1,0,-1):
		print(i)	
		swap(values,0,i)
		print(values)
		n = n-1
		heapify(values,n,0)
	return values

print(sort(build_heap(a,len(a))))
	
