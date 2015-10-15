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

with open('testSet.csv', 'rb') as csvfile:
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
	s = 'c'+str(i)
	rows.append(s)


#---------------SET PRIORITY VALUES HERE-------------------------------

priority = [0.7,0.3,0.2,-0.5,0.4]
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

pessimisticPriorityTable = []
optimisticPriorityTable = []
neutralPriorityTable = []

for each in fuzzySet:
	tempListForPessimistic = []
	tempListForOptimistic = []
	tempListForNeutral = []

	for i in xrange(len(each)):
		a = each[i][0]*priority[i]
		b = each[i][1]*priority[i]
		c = ((each[i][0]+each[i][1])/2) * priority[i]

		tempListForPessimistic.append(a)
		tempListForOptimistic.append(b)
		tempListForNeutral.append(c)

	pessimisticPriorityTable.append(tempListForPessimistic)
	optimisticPriorityTable.append(tempListForOptimistic)
	neutralPriorityTable.append(tempListForNeutral)

print "Priority Table for pessmistic values"
for each in pessimisticPriorityTable:
	print each

print "Priority Table for optimistic values"
for each in optimisticPriorityTable:
	print each

print "Priority Table for neutral values"
for each in neutralPriorityTable:
	print each

savedPessimisticPriorityTable = list(pessimisticPriorityTable)
savedOptimisticPriorityTable = list(optimisticPriorityTable)
savedNeutralPriorityTable = list(neutralPriorityTable)

#------------------------------Get Row Sum of Priority Table -----------------
print 
pessimisticRowSum = []
optimisticRowSum = []
neutralRowSum = []

for each in pessimisticPriorityTable:
	pessimisticRowSum.append(sum(each))

for each in optimisticPriorityTable:
	optimisticRowSum.append(sum(each))

for each in neutralPriorityTable:
	neutralRowSum.append(sum(each))

print "Row Sum of Pessmmistic Priority Table"
print pessimisticRowSum

print "Row Sum of Optimistic Priority Table"
print optimisticRowSum

print "Row Sum of Neutrala priority table"
print neutralRowSum


#----------------------------Get Comparision Table -------------------------
print 
#print "Comparision Table"

pessimisticComparisionTable = []
optimisticComparisionTable = []
neutralComparisionTable = []

for each in pessimisticPriorityTable:
	a = sum(each)
 	temp = []
 	for each in pessimisticPriorityTable:
		b = sum(each)
		temp.append(a-b)
	pessimisticComparisionTable.append(temp)

for each in optimisticPriorityTable:
	a = sum(each)
 	temp = []
 	for each in optimisticPriorityTable:
		b = sum(each)
		temp.append(a-b)
	optimisticComparisionTable.append(temp)

for each in neutralPriorityTable:
	a = sum(each)
 	temp = []
 	for each in neutralPriorityTable:
		b = sum(each)
		temp.append(a-b)
	neutralComparisionTable.append(temp)


print "pessmisitic comparision table"
for each in pessimisticComparisionTable:
	print each 
#--------------------------Semi Final Result-----------------
print 

rowSumPessimisticComparisionTable = []
rowSumOptimisticComparisionTable = []
rowSumNeutralComparisionTable = []

for each in pessimisticComparisionTable:
	rowSumPessimisticComparisionTable.append(sum(each))

for each in optimisticComparisionTable:
	rowSumOptimisticComparisionTable.append(sum(each))

for each in neutralComparisionTable:
	rowSumNeutralComparisionTable.append(sum(each))


semiFinalResults = []
semiFinalResults.append(rowSumPessimisticComparisionTable)
semiFinalResults.append(rowSumOptimisticComparisionTable)
semiFinalResults.append(rowSumNeutralComparisionTable)

print semiFinalResults
# #----------------------Alteration to result to check algorithm------------
# # semiFinalResult[0] = semiFinalResult[1]
# # semiFinalResult[2] = semiFinalResult[1]
# # priorityTable[0][0] = priorityTable[1][0]
# print semiFinalResult

#------------------------------Scores calculated------------
scores = semiFinalResults

#-----------------------------The list has been sorted based on score----------

savedSemiFinalResults = list(semiFinalResults)
print savedSemiFinalResults

sortedOrder = []
count = 0
for savedSemiFinalResult in savedSemiFinalResults:
	print count 
	count +=1
	print savedSemiFinalResult
	score = savedSemiFinalResult
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
						maxValue = pessimisticPriorityTable[sortOrder[startIndex]][y]


						for x in xrange(startIndex, i):
							if pessimisticPriorityTable[sortOrder[x]][y] > maxValue:
								maxIndex = sortOrder[x]
								maxValue = pessimisticPriorityTable[maxIndex][y]						

						if maxIndex == startIndex and pessimisticPriorityTable[sortOrder[startIndex]][y] == pessimisticPriorityTable[sortOrder[startIndex]+1][y]:
								break
						else:
							order.append(maxIndex)
							pessimisticPriorityTable[maxIndex][y] = -999
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

	sortedOrder.append(sortOrder)

finalList = []
for sortOrder in sortedOrder:
	tempFinalList = []
	for i in xrange(len(sortOrder)):
		rank = sortOrder.index(i)
		tempFinalList.append(rank+1)
	finalList.append(tempFinalList)

ranks = list(finalList)

score = []
for i in xrange(len(ranks[0])):
	scoreSum = 0
	for j in xrange(len(ranks)):
		scoreSum+=ranks[j][i]
	score.append(scoreSum)

print score

savedScore = list(score)

print savedScore

#----------Sort this it out -----------

finalRankList = []
finalScoreRankList = []
for i in xrange(len(savedScore)):
	maxi = max(savedScore)
	maxiIndex = savedScore.index(maxi)

	savedScore[maxiIndex] = -9999
	finalScoreRankList.append(maxi)
	finalRankList.append(maxiIndex)

print "final rank list" , finalRankList
print "final score rank list ", finalScoreRankList

savedScore = list(score)
#-----------------tie breaker-----------

def calculateScore(c, p):
	candidateScore = fuzzySets[c][p][0]
	return candidateScore

startIndex = 0
for i in xrange(len(savedScore)):
	if finalScoreRankList[i] == finalScoreRankList[startIndex]:
		pass
	else:
		if i-startIndex > 1:
			for p in xrange(len(priority)):
				candidateScores = []
				for c in xrange(startIndex,i):
					candidateScores.append(calculateScore(c,p))
				
				if len(candidateScores)!=len(set(candidateScores)):
					continue
				else:
					finList = []
					for d in xrange(len(candidateScores)):
						maxi = candidateScores[0]
						maxiIndex = 0
						for b in xrange(len(candidateScores)):
							if candidateScores[b] > maxi:
								maxi = candidateScores[b]
								maxiIndex = b
						finList.append(maxiIndex)
						candidateScores[maxiIndex] = -99999
					for each in finList:
						each+startIndex
					originalList = list(finalRankList)
					
					for g in xrange(len(candidateScores)):
						print "value of g ", g
						minNum = min(finList)
						minIndex = finList.index(minNum)
						print "minimum value ", minNum, "minIndex ", minIndex
						finalRankList[startIndex+g]= originalList[minIndex]
						finList[minIndex] = 9999

					startIndex = i
					break
		else:
			startIndex = i
print finalRankList
for each in reversed(finalRankList):
	print rows[each]


# #-------------------------------------Write result to file---------------------------------------------
# with open('result.csv', 'wb') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=',',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     firstRow = []
#     secondRow = []

#     firstRow.append("")
#     for each in parameters:
#     	firstRow.append(each)
#     firstRow.append("Score")
#     spamwriter.writerow(firstRow)
    
#     secondRow.append("")
#     for each in priority:
#     	secondRow.append(each)
#     	secondRow.append(each)
#     spamwriter.writerow(secondRow)

#     for i in xrange(len(rows)):
#     	temp = []
#     	temp.append(rows[i])
#     	for para in fuzzySet[i]:
#     		for each in para:
# 	    		temp.append(each)
#     	temp.append(semiFinalResult[i])
#     	spamwriter.writerow(temp)

# with open('order.csv', 'wb') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=',',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
#     for each in sortOrder:
#     	temp = []
#     	temp.append(rows[each])
#     	temp.append(semiFinalResult[each])
#     	spamwriter.writerow(temp)