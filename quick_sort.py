
import sys
sys.setrecursionlimit(10000000)
###################################################
##################  quick sort ####################
def partition(li, left, right):
	##### this is for the worst case. However, it  doesnt
	##### change the worst time complexity o(n^2)
	ranid = random.randint(left,right)
	li[randid], li[left] = li[left], li[ranid]

	tmp = li [left]
	while left < right:
		while left < right and li[right] >= tmp:
			right -= 1
		li[left] = li[right]
		while left < right and li[left] <= tmp:
			left += 1
		li[right] = li[left]

def quick_sort(li, left, right):
	if left < right:
		mid = partition(li, left, right)
		quick_sort(li, left, mid - 1)
		quick_sort(li, mid + 1, right)

### the normal time complexity of the quick sort is o(n*log(n))
### however the worst case the time complexity is o(n^2)

### for python the quick_sort has a iterattion problem. when there r too many
### iteration the sys.setrecursionlimit would need to be set. sometimes it will
### even crahs the program