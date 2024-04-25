def max_of_two(x, y):
	if x>y:
		return x
	elif x<y:
		return y
	if x==y:
		return x or y

def max_of_three(x, y, z):
	if (x>y) and (x>z):
		return x
	elif (y>x) and (y>z):
		return y
	elif (z>x) and (z>y):
		return z
	if x==y==z:
		return x or y or z
		
print(max_of_two(5,4))

print(max_of_two(-2,-3))

print(max_of_two(0,0))

print(max_of_three(5,4,7))

print(max_of_three(-2,-3,-1))

print(max_of_three(0,0,0))
