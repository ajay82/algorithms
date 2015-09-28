# Given a string, pring all possible palindromes that can be constructred from subsequences

def print_recursive_substring(input, palindrome):
		if (input == '' or len(input) == 0):
				if (palindrome != ''):
						print palindrome + palindrome[::-1]
						return
				else:
						return

		if (len(input) == 1):
				if (len(palindrome) > 0):
						print palindrome + input + palindrome[::-1]
						print palindrome + palindrome[::-1]
						return
				else:
						print input
						return

		if (input[0] == input[len(input)-1]):
						print_recursive_substring(input[1:len(input)-1], palindrome + input[0])
						print_recursive_substring(input[1::], palindrome)
						return


		print_recursive_substring(input[1::], palindrome)	
		print_recursive_substring(input[0:len(input)-1], palindrome)

input_list = ['a', 'aba', 'c', 'cd', 'bb', 'abccba', 'abcefcba']
for input in input_list:
		print "For input: " + input
		print_recursive_substring(input, '')
		print "End \n"
