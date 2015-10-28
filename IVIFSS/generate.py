import random
import csv

j = input("Enter the number of judges: ")
n = input("Enter the number of parameters: ")
parameters = []
nn = n
while(n):
	parameter = raw_input("Enter parameter : ") 
	parameters.append(parameter + " m-")
	parameters.append(parameter + " m+")
	parameters.append(parameter + " n-")
	parameters.append(parameter + " n+")
	parameters.append(parameter + " h-")
	parameters.append(parameter + " h+")
	n-=1
n = nn
m = input("Enter the number of values you want to randomly generate : ")

def createSet(num):
	fuzzySet = []
	for i in xrange(m):
		temp = []
		for j in xrange(n):
			temp2 = []
			mplus = "%.2f"%random.random()
			mminus = "%.2f"%random.uniform(float(mplus),1)
			nPlusRange = 1-float(mminus)
			nplus = "%.2f"%random.uniform(0,float(nPlusRange))
			nMinusRange = 1-float(mplus)
			nminus = "%.2f"%random.uniform(float(nplus),float(nMinusRange))
			hplus = 1-float(mminus)-float(nminus)
			hminus = 1-float(mplus)-float(nplus)
			temp2.append(mplus)
			temp2.append(mminus)
			temp2.append(nplus)
			temp2.append(nminus)
			temp2.append(hplus)
			temp2.append(hminus)		
			temp.append(temp2)
		fuzzySet.append(temp)
	for each in fuzzySet:
		print each 

	with open('testSet'+ str(num) +'.csv', 'wb') as csvfile:
	    spamwriter = csv.writer(csvfile, delimiter=',',
	                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
	    spamwriter.writerow(parameters)
	    for row in fuzzySet:
	    	tempRow = []
	    	for para in row:
	    		for each in para:
	    			tempRow.append(each)
	    	spamwriter.writerow(tempRow)

for i in xrange(j):
	createSet(i)