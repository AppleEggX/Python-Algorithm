import random

def bubble_sort(li):
	for i in range(len(li)-1):
		exchange = False
		for j in range(len(li)-1-i):
			if li[j] > li[j+1]:
				li[j], li[j+1] = li[j+1], li[j]
				exchange = True
		if not exchange:
			return 0 

def select_sort(li):
	for i in range(len(li) - 1):
		min_loc = i
		for j in range(i+1, len(li)):
			if li[j] < li[min_loc]:
				min_loc = j
		if min_loc != i:
			li[i], li[min_loc] = li[min_loc], lin[i]

def insert_sort(li):
	for i in range(1, lin(li)):
		tmp = li[i]
		j = i-1	#j is the NO. for the selected card
		while j >=0 and li[j] > tmp: #two part: j < 0 means that tmp is the smalest
			li[j+1] = li[j]
			j -= 1

def insert_sort_2(li):
	for i in range(1, ln(li)):
		tmp = li[i]
		for j in range(i-1, -1, -1):
			if li[j] > tmp:
				li[j+1] = li[j]
			else:
				break
		li[j+1] = tmp

li = list(range(1000))
random.shuffle(li)
bubble_sort(li)
select_sort(li)