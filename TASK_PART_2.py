# _______PART II_______
# ----1
def return_the_sum(start, end):
	return sum(range(start, end+1))

print(return_the_sum(1, 10))

# ----2
list1 = [1, 2, 3, 4, 5]

def multi(l):
	res = 1
	for i in l:
		res *= i
	return res

print(multi(list1))

# ----3
list1 = [1, 2, 3, 4, 5]

def minimum(l):
	return min(l)

print(minimum(list1))

# ----4
list1 = [1, 2, 3, 4, 5]

def prime_numbers(l):
	prime_nums = 0
	times = 0
	for i in l:
		if i < 2:
			continue
		for j in range(1, i+1):
			if i % j == 0:
				times += 1
		if times == 2:
			prime_nums += 1
		times = 0
	return prime_nums

print(f"There are {prime_numbers(list1)} prime numbers in this list.")

# ----5
list1 = [1, 2, 3, 4, 5, 4, 3, 4, 3, 2, 3, 4, 3, 2, 1]
n = int(input("Enter the element you want to delete > "))

def delete_item(l, item):
	count = 0
	for i in l:
		if i == item:
			list1.remove(i)
			count += 1
	return count

print(f"Removed {delete_item(list1, n)} items.")
print(f'(Output list: {", ".join(map(str, list1))})')

# ----6
list1 = [1, 3, 5, 7, 9]
list2 = [5, 7, 8, 9, 11]

def conjure_without_duplicates(l1, l2):
	reslist = []
	for i in l1:
		reslist.append(i)
	for i in l2:
		if i not in reslist:
			reslist.append(i)
	return reslist

def conjure(l1, l2): # I made this one just in case if I understood the task wrong
	return l1+l2

print(f"Conjured list: {', '.join(map(str, conjure_without_duplicates(list1, list2)))}")

# ----7
list1 = [1, 2, 3, 4, 5]

def rise(l, c):
	reslist = []
	for i in l:
		reslist.append(i**c)
	return reslist

print(f"Here are the results: {', '.join(map(str, rise(list1, 2)))}")
