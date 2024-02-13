# -*- coding: utf-8 -*- 

unsorted_list = [20, 7, 3, 4, 12, 15, 2, 1]

#Selection Sort 

#Pseudocode

# for j ← 1 to n-1
# 	smallest ← j
#     for i ← j + 1 to n
# 	    if A[ i ] < A[ smallest ]
#             smallest ← i    
#     Exchange A[ j ] ↔ A[ smallest ]

def selection_sort(a):
	for j in range(len(a)-1):
		minimum = j #assume that element with j index is minimum
		for i in range(j+1, len(a)): #compare it with unsorted elements(we leave the sorted elements behind) 
			if(a[i]<a[minimum]):
				minimum = i #update minimum index with the smaller element
		a[j],a[minimum]=a[minimum],a[j] #swap the elements that are assumed minimum and actual minimum found in unsorted list
	print("after selection sort:")
	print(a)

selection_sort(unsorted_list)



