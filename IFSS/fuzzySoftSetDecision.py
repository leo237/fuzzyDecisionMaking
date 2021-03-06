#---------Taking Raw input------------

# numberOfParameters = raw_input("Enter the number of Parameters you want to enter : ")
# numberOfHouses = raw_input("Enter the number of houses : ");

# parameters = []
# for i in xrange(numberOfParameters):
# 	name = raw_input("Enter parameter " + i + " :")
# 	parameters.append(name)

# fuzzySet = []

# for i in xrange(numberOfHouses):
# 	tempList = []
# 	for each in xrange(numberOfParameters):
# 		a = input()
# 		tempList.append(a)
# 	fuzzySet.append(tempList)

# priority = []
# for i in xrange(numberOfParameters):
# 	p = input()
# 	priority.append(p)

#-----------------------------Standart Input--------------
# numberOfParameters = 5
# numberOfHouses = 6
# parameters = ["Beautiful","Wooden","Green Surrounded", "Expensive", "Distance"]
# rows = ["h1","h2","h3","h4","h5","h6"]
# fuzzySet = [[0.1,0,0.2,0.1,0.8],[0.9,0.6,0.8,0.8,0.3],[0.3,0.1,0.2,0.3,0.4],[0.7,0.7,0.6,0.6,0.6],[0.3,0.4,0.4,0.5,0.1],[0.9,0.5,0.6,0.6,0.5]]


#-------------------------Importing Input from CSV File------------------
import csv 

parameters = []
fuzzySet = []
rows = []
counter = 0

with open('generatedValues.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		if counter == 0:
			parameters = list(row)
		else:
			temp = []
			counter = 0
			temp2 = []	
			for each in row:
				if (counter%2 == 0):
					temp2.append(float(each))
				else:
					temp2.append(float(each))
					temp.append(temp2)
					temp2 = []
				counter+=1
			fuzzySet.append(temp)
		counter+=1

numberOfParameters = len(parameters)/2
numberOfHouses = len(fuzzySet)

for i in xrange(1,numberOfHouses+1):
	s = 'h'+str(i)
	rows.append(s)


#---------------SET PRIORITY VALUES HERE-------------------------------

priority = [0.7,0.0,0.2,-0.5,-0.2]
#----------------------------------------------------------------------

priorityOrder = []

limit = len(priority)
i = 0
while i < limit:
	if priority[i] == 0:
		del priority[i]
		for each in fuzzySet:
			del each[i]
		del parameters[2*i]
		del parameters[(2*i)]
		limit-=1
	i+=1

#----------------Sort Priority Order-------------
savedPriority = []
for each in priority:
	savedPriority.append(abs(each))

for each in savedPriority:
	maxPriority = max(savedPriority)
	maxPriorityIndex = savedPriority.index(maxPriority)
	savedPriority[maxPriorityIndex] = -99
	priorityOrder.append(maxPriorityIndex)
#-----------------Calculate Priority Table--------------------------------

membershipPriorityTable = []
nonMembershipPriorityTable = []
hesitationPriorityTable = []

for each in fuzzySet:
	tempListForMembership = []
	tempListForNonMembership = []
	tempListForHesitation = []

	for i in xrange(len(each)):
		a = each[i][0]*priority[i]
		b = each[i][1]*priority[i]
		c = (1 - (each[i][0] + each[i][1]) ) * priority[i]

		tempListForMembership.append(a)
		tempListForNonMembership.append(b)
		tempListForHesitation.append(c)

	membershipPriorityTable.append(tempListForMembership)
	nonMembershipPriorityTable.append(tempListForNonMembership)
	hesitationPriorityTable.append(tempListForHesitation)

print "Priority Table for membership values"
for each in membershipPriorityTable:
	print each

print "Priority Table for non membership values"
for each in nonMembershipPriorityTable:
	print each

print "Priority Table for hesitation values"
for each in hesitationPriorityTable:
	print each

savedMembershipPriorityTable = list(membershipPriorityTable)
savedNonMembershipPriorityTable = list(nonMembershipPriorityTable)
savedHesitationPriorityTable = list(hesitationPriorityTable)

#------------------------------Get Row Sum of Priority Table -----------------
print 
membershipRowSum = []
nonMembershipRowSum = []
hesitationRowSum = []

for each in membershipPriorityTable:
	membershipRowSum.append(sum(each))

for each in nonMembershipPriorityTable:
	nonMembershipRowSum.append(sum(each))

for each in hesitationPriorityTable:
	hesitationRowSum.append(sum(each))

print "Row Sum of Membership Priority Table"
print membershipRowSum

print "Row Sum of Non Membership Priority Table"
print nonMembershipRowSum

print "Row Sum of hesitiation priority table"
print hesitationRowSum


#----------------------------Get Comparision Table -------------------------
print 
#print "Comparision Table"

membershipComparisionTable = []
nonMembershipComparisionTable = []
hesitationComparisionTable = []

for each in membershipPriorityTable:
	a = sum(each)
 	temp = []
 	for each in membershipPriorityTable:
		b = sum(each)
		temp.append(a-b)
	membershipComparisionTable.append(temp)

for each in nonMembershipPriorityTable:
	a = sum(each)
 	temp = []
 	for each in nonMembershipPriorityTable:
		b = sum(each)
		temp.append(a-b)
	nonMembershipComparisionTable.append(temp)

for each in hesitationPriorityTable:
	a = sum(each)
 	temp = []
 	for each in hesitationPriorityTable:
		b = sum(each)
		temp.append(a-b)
	hesitationComparisionTable.append(temp)

#--------------------------Semi Final Result-----------------
print 

rowSumMembershipComparisionTable = []
rowSumNonMembershipComparisionTable = []
rowSumHesitiationComparisionTable = []

for each in membershipComparisionTable:
	rowSumMembershipComparisionTable.append(sum(each))

for each in nonMembershipComparisionTable:
	rowSumNonMembershipComparisionTable.append(sum(each))

for each in hesitationComparisionTable:
	rowSumHesitiationComparisionTable.append(sum(each))

semiFinalResult = []
for i in xrange(len(rowSumMembershipComparisionTable)):
	ans = (rowSumMembershipComparisionTable[i] - rowSumNonMembershipComparisionTable[i] + rowSumHesitiationComparisionTable[i] + 1 ) /2
	semiFinalResult.append(ans)

print semiFinalResult
# #----------------------Alteration to result to check algorithm------------
# # semiFinalResult[0] = semiFinalResult[1]
# # semiFinalResult[2] = semiFinalResult[1]
# # priorityTable[0][0] = priorityTable[1][0]
# print semiFinalResult

#------------------------------Scores calculated------------
score = semiFinalResult

#-----------------------------The list has been sorted based on score----------

savedSemiFinalResult = list(semiFinalResult)
sortOrder = []
for i in xrange(len(savedSemiFinalResult)):
	highestValue = max(savedSemiFinalResult)
	
	highestValueIndex = savedSemiFinalResult.index(highestValue)	
	savedSemiFinalResult[highestValueIndex] = -99999
	sortOrder.append(highestValueIndex)

print sortOrder
print 

print "Approximate order of preference without tie breaker rule"
for each in sortOrder:
	print rows[each]
#------------------------------Tie Breaker----------------------------------------
startIndex = 0
endIndex = len(sortOrder)

for i in xrange(len(sortOrder)-1):
	if score[sortOrder[startIndex]] == score[sortOrder[i]]:
		continue
	else:
		if i-startIndex > 1:
			needToCheckY = 1
			for y in priorityOrder:
				order = []
				for t in xrange(i-startIndex):
					maxIndex = sortOrder[startIndex]
					maxValue = membershipPriorityTable[sortOrder[startIndex]][y]

					for x in xrange(startIndex, i):
						if membershipPriorityTable[sortOrder[x]][y] > maxValue:
							maxIndex = sortOrder[x]
							maxValue = membershipPriorityTable[maxIndex][y]						

					if maxIndex == startIndex and membershipPriorityTable[sortOrder[startIndex]][y] == membershipPriorityTable[sortOrder[startIndex]+1][y]:
							break
					else:
						order.append(maxIndex)
						membershipPriorityTable[maxIndex][y] = -999
						needToCheckY = 0
					print
				if needToCheckY == 0:
					break 
			tempSortOrder = []
			for b in xrange(startIndex):
				tempSortOrder.append(sortOrder[b])

			for b in order:
				tempSortOrder.append(b)

			for b in xrange(i,endIndex):
				tempSortOrder.append(sortOrder[b])

			sortOrder = list(tempSortOrder) 
			startIndex = i
			print "Sorted Order : ", sortOrder
		else:
			startIndex = i 	

print "Final result :"
for each in sortOrder:
	print rows[each]

#-------------------------------------Write result to file---------------------------------------------
with open('result.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    firstRow = []
    secondRow = []

    firstRow.append("")
    for each in parameters:
    	firstRow.append(each)
    firstRow.append("Score")
    spamwriter.writerow(firstRow)
    
    secondRow.append("")
    for each in priority:
    	secondRow.append(each)
    	secondRow.append(each)
    spamwriter.writerow(secondRow)

    for i in xrange(len(rows)):
    	temp = []
    	temp.append(rows[i])
    	for para in fuzzySet[i]:
    		for each in para:
	    		temp.append(each)
    	temp.append(semiFinalResult[i])
    	spamwriter.writerow(temp)

with open('order.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    for each in sortOrder:
    	temp = []
    	temp.append(rows[each])
    	temp.append(semiFinalResult[each])
    	spamwriter.writerow(temp)