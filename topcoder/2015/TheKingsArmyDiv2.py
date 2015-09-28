# Question : http://community.topcoder.com/stat?c=problem_statement&pm=13597&rd=16086
# http://apps.topcoder.com/wiki/display/tc/SRM+643

print "Start.."

class TheKingsArmyDiv2:
	def getNumber(self, inputStrings):
		count_happy = 0
		count_sad = 0;
		for row in inputStrings:
			for i in range(len(row)-1):							 
				if (row[i] == 'H'):
					if (row[i+1] == 'H'):
						return 0
					count_happy += 1
				else:
					count_sad += 1
		if count_sad > 0:
			if (count_happy > 0 and len(inputStrings[0]) > 1):
				return 1
			return count_sad	
		else:
			return 0

input = [];
input.append('SSSSS')
input.append('SSHHS')
input.append('SSSSS')

x = TheKingsArmyDiv2()
result = x.getNumber(input);
print result


