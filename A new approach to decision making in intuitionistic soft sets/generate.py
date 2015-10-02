import random
import csv

n = input("Enter the number of parameters: ")
parameters = []
nn = n
while(n):
	parameter = raw_input("Enter parameter : ") 
	parameters.append(parameter + " mu")
	parameters.append(parameter + " nu")
	n-=1
n = nn
m = input("Enter the number of values you want to randomly generate : ")

fuzzySet = []
for i in xrange(m):
	temp = []
	for j in xrange(n):
		temp2 = []
		membership = "%.2f"%random.random()
		nonMembershipRange = 1-float(membership)
		nonmembership = "%.2f"%random.uniform(0,nonMembershipRange)
		temp2.append(membership)
		temp2.append(nonmembership)
		
		temp.append(temp2)
	fuzzySet.append(temp)

print fuzzySet


with open('generatedValues.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(parameters)
    for row in fuzzySet:
    	tempRow = []
    	for para in row:
    		for each in para:
    			tempRow.append(each)
    	spamwriter.writerow(tempRow)