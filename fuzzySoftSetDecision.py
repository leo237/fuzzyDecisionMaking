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

numberOfParameters = 5
numberOfHouses = 6
parameters = ["Beautiful","Wooden","Green Surrounded", "Expensive", "Distance"]
rows = ["h1","h2","h3","h4","h5","h6"]
fuzzySet = [[0.1,0,0.2,0.1,0.8],[0.9,0.6,0.8,0.8,0.3],[0.3,0.1,0.2,0.3,0.4],[0.7,0.7,0.6,0.6,0.6],[0.3,0.4,0.4,0.5,0.1],[0.9,0.5,0.6,0.6,0.5]]

priority = [0.7,0.0,0.2,-0.5,-0.2]

priorityOrder = []

limit = len(priority)
i = 0
while i < limit:
	if priority[i] == 0:
		del priority[i]
		for each in fuzzySet:
			del each[i]
		del parameters[i]
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

#-------------------------------------------------

priorityTable = []

for each in fuzzySet:
	tempList = []
	for i in xrange(len(each)):
		a = each[i]*priority[i]
		tempList.append(a)
	priorityTable.append(tempList)

print "Priority Table"
for each in priorityTable:
	print each

savedPriorityTable = list(priorityTable)
#------------------------------Get Row Sum of Priority Table -----------------
print 
rowSum = []
print "Row Sum of Priority Table"
for each in priorityTable:
	rowSum.append(sum(each))

print rowSum

#----------------------------Get Comparision Table -------------------------
print 
print "Comparision Table"

comparisionTable = []
for each in priorityTable:
	a = sum(each)
 	temp = []
 	for each in priorityTable:
		b = sum(each)
		temp.append(a-b)
	comparisionTable.append(temp)

for each in comparisionTable:
	print each

#--------------------------Final Result-----------------
print 

semiFinalResult = []
print "Semi final Result"
for each in comparisionTable:
	semiFinalResult.append(sum(each))

semiFinalResult[0] = semiFinalResult[1]
semiFinalResult[2] = semiFinalResult[1]
priorityTable[0][0] = priorityTable[1][0]


print semiFinalResult
#------------------------------Scores calculated------------
score = semiFinalResult

#-----------------------------The list has been sorted based on score----------
savedSemiFinalResult = list(semiFinalResult)
sortOrder = []
for i in xrange(len(savedSemiFinalResult)):
	highestValue = max(savedSemiFinalResult)
	
	highestValueIndex = savedSemiFinalResult.index(highestValue)	
	savedSemiFinalResult[highestValueIndex] = -9999
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
					maxValue = priorityTable[sortOrder[startIndex]][y]

					for x in xrange(startIndex, i):
						if priorityTable[sortOrder[x]][y] > maxValue:
							maxIndex = sortOrder[x]
							maxValue = priorityTable[maxIndex][y]
						

					if maxIndex == startIndex and priorityTable[sortOrder[startIndex]][y] == priorityTable[sortOrder[startIndex]+1][y]:
							break
					else:
						order.append(maxIndex)
						priorityTable[maxIndex][y] = -999
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