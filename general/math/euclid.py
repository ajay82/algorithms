
def gcd(a, b):
	if (a == 0):
		return b
	return gcd(b%a, a)


input_list = [[5,2], [14,7]]

for input in input_list:
	print 'input: ', input, ', output: ', gcd(*input)	

