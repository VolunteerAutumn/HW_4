# ______PART I______
# ----1
def motivational_quote():
	print("\"Don't complare yourself with anyone in this world...\n\tif you do so, you are insulting yourself.\"\n\t\tBill Gates")
	
motivational_quote()

# ----2
def get_even_from_range(start, end):
	reslist = []
	for i in range(start, end+1):
		if i % 2 == 0:
			reslist.append(i)
	return reslist

print(f"Here are the even numbers! > {', '.join(map(str, get_even_from_range(0, 10)))}.")

# ----3
def draw_square(length, symbol, is_filled):
	if is_filled:
		for i in range(length):
			print(f"{symbol}  "*length)
	else:
		print(f"{symbol}  "*length)
		for i in range(length-2):
			print(f"{symbol}  " + "   "*(length-2) + f"{symbol}  ")
		print(f"{symbol}  " * length)
			
draw_square(10, "%", False)

# ----4
def retmin(*numbers):
	return min(numbers)

print(f"Min: {retmin(1, 3, 4, 5, 6, -4)}")

# ----5
def count_digs(x):
	l = len(str(x))
	if "." in str(x):
		l -= 1
	return l

print(f"The number you typed consists of {count_digs(33.125)} digits.")

# ----6
def is_palindrome(x):
	if str(x) == str(x)[::-1]:
		return True
	else:
		return False
	
if is_palindrome(123321):
	print("It is a palindrome!")
else:
	print("It is not a palindrome.")
	
if is_palindrome(123456):
	print("It is a palindrome!")
else:
	print("It is not a palindrome.")
