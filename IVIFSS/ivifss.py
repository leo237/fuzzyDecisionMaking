import csv 

def calculateRankList(judgeInput):

	parameters = []
	fuzzySet = []
	rows = []
	counter = 0

	with open(judgeInput+'.csv', 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in spamreader:
			if counter == 0:
				parameters = list(row)
			else:
				temp = []
				counter = 0
				tempCounter = 0
				tempCounter = 0

				temp2 = []	
				temp3 = []
				for each in row:
					if (counter%2 == 0):
						temp2.append(float(each))
					else:
						temp2.append(float(each))
						temp.append(temp2)
						tempCounter+=1
						temp2 = []
					counter+=1
					if tempCounter == 3:
						tempCounter = 0
						temp3.append(temp)
						temp = []
				fuzzySet.append(temp3)
			counter+=1

	numberOfParameters = len(parameters)/2
	numberOfHouses = len(fuzzySet)

	for i in xrange(1,numberOfHouses+1):
		s = 'c'+str(i)
		rows.append(s)


	#---------------SET PRIORITY VALUES HERE-------------------------------

	priority = [0.3,0.2,-0.1,0.15,0.35,0]
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

	#print "Priority Order ", priorityOrder
	#-------------------Constructing required tables--------------

	optimisticTable = []
	pessimisticTable = []
	neutralTable = []

	for each in fuzzySet:
		rowOpti=  []
		rowPessi = []
		rowNeu = []
		for parameter in each:
			tempOptimisticTable = []
			tempPessimisticTable = []
			tempNeutralTable = []

			tempOptimisticTable.append(parameter[0][1])
			tempOptimisticTable.append(parameter[1][0])
			tempOptimisticTable.append(1-parameter[0][1]-parameter[1][0])

			tempPessimisticTable.append(parameter[0][0])
			tempPessimisticTable.append(parameter[1][1])
			tempPessimisticTable.append(1-parameter[0][0]-parameter[1][1])

			tempNeutralTable.append((parameter[0][0]+parameter[0][1])/2)
			tempNeutralTable.append((parameter[1][0]+parameter[1][1])/2)
			tempNeutralTable.append(1-((parameter[0][0]+parameter[0][1])/2)-((parameter[1][0]+parameter[1][1])/2))

			rowOpti.append(tempOptimisticTable)
			rowPessi.append(tempPessimisticTable)
			rowNeu.append(tempNeutralTable)
			
		optimisticTable.append(rowOpti)
		pessimisticTable.append(rowPessi)
		neutralTable.append(rowNeu)


	#------------Calculating priority tables---------------

	pessimisticPriorityTable = []
	optimisticPriorityTable = []
	neutralPriorityTable = []


	for row in optimisticTable:
		tempListForOptimistic = []
		for parameter in xrange(len(row)):
			tempList = []
			for each in row[parameter]:
				tempList.append(each*priority[parameter])
			tempListForOptimistic.append(tempList)
		optimisticPriorityTable.append(tempListForOptimistic)


	for row in pessimisticTable:
		tempListForPessimistic = []
		for parameter in xrange(len(row)):
			tempList = []
			for each in row[parameter]:
				tempList.append(each*priority[parameter])
			tempListForPessimistic.append(tempList)
		pessimisticPriorityTable.append(tempListForPessimistic)

	for row in neutralTable:
		tempListForNeutral = []
		for parameter in xrange(len(row)):
			tempList = []
			for each in row[parameter]:
				tempList.append(each*priority[parameter])
			tempListForNeutral.append(tempList)
		neutralPriorityTable.append(tempListForNeutral)


	#-------------Row Sum of Priority Tables----------

	rowSumOptimisticMem = []
	rowSumOptimisticNon = []
	rowSumOptimistictHes = []

	rowSumPessimisticMem = []
	rowSumPessimisticNon = []
	rowSumPessimisticHes = []

	rowSumNeutralMem = []
	rowSumNeutralNon = []
	rowSumNeutralHes = []

	for each in optimisticPriorityTable:
		sumMem = 0
		sumNon = 0
		sumHes = 0
		for parameter in each:
			sumMem += parameter[0]
			sumNon += parameter[1]
			sumHes += parameter[2]
		rowSumOptimisticMem.append(sumMem)
		rowSumOptimisticNon.append(sumNon)
		rowSumOptimistictHes.append(sumHes)

	for each in pessimisticPriorityTable:
		sumMem = 0
		sumNon = 0
		sumHes = 0
		for parameter in each:
			sumMem += parameter[0]
			sumNon += parameter[1]
			sumHes += parameter[2]
		rowSumPessimisticMem.append(sumMem)
		rowSumPessimisticNon.append(sumNon)
		rowSumPessimisticHes.append(sumHes)

	for each in neutralPriorityTable:
		sumMem = 0
		sumNon = 0
		sumHes = 0
		for parameter in each:
			sumMem += parameter[0]
			sumNon += parameter[1]
			sumHes += parameter[2]
		rowSumNeutralMem.append(sumMem)
		rowSumNeutralNon.append(sumNon)
		rowSumNeutralHes.append(sumHes)

	rowSumOptimistic = []
	rowSumPessimistic = []
	rowSumNeutral = []
	rowSumOptimistic.append(rowSumOptimisticMem)
	rowSumOptimistic.append(rowSumOptimisticNon)
	rowSumOptimistic.append(rowSumOptimistictHes)

	rowSumPessimistic.append(rowSumPessimisticMem)
	rowSumPessimistic.append(rowSumPessimisticNon)
	rowSumPessimistic.append(rowSumPessimisticHes)

	rowSumNeutral.append(rowSumNeutralMem)
	rowSumNeutral.append(rowSumNeutralNon)
	rowSumNeutral.append(rowSumNeutralHes)

	#--------------Comparision Tables-----------------

	pessimisticComparisionTable = []
	optimisticComparisionTable = []
	neutralComparisionTable = []

	for i in xrange(len(rows)):
		rowComparision = []
		for j in xrange(len(rows)):
			eachParameter = []
			for k in xrange(3):
				val = rowSumOptimistic[k][i]-rowSumOptimistic[k][j]
				eachParameter.append(val)
			rowComparision.append(eachParameter)
		optimisticComparisionTable.append(rowComparision)

	for i in xrange(len(rows)):
		rowComparision = []
		for j in xrange(len(rows)):
			eachParameter = []
			for k in xrange(3):
				val = rowSumPessimistic[k][i]-rowSumPessimistic[k][j]
				eachParameter.append(val)
			rowComparision.append(eachParameter)
		pessimisticComparisionTable.append(rowComparision)

	for i in xrange(len(rows)):
		rowComparision = []
		for j in xrange(len(rows)):
			eachParameter = []
			for k in xrange(3):
				val = rowSumNeutral[k][i]-rowSumNeutral[k][j]
				eachParameter.append(val)
			rowComparision.append(eachParameter)
		neutralComparisionTable.append(rowComparision)
	 

	#-------------------------Decision Table------------------------------

	dtOptimistic = []
	dtPessimistic = []
	dtNeutral = []

	def score(mu, h):
		return mu*(1+h)

	for row in optimisticComparisionTable:
		msum = 0
		nsum = 0
		hsum = 0
		for parameter in row:
			msum += parameter[0]
			nsum += parameter[1]
			hsum += parameter[2]

		dtOptimistic.append([msum,nsum,hsum,score(msum,hsum)])

	for row in pessimisticComparisionTable:
		msum = 0
		nsum = 0
		hsum = 0
		for parameter in row:
			msum += parameter[0]
			nsum += parameter[1]
			hsum += parameter[2]
		dtPessimistic.append([msum,nsum,hsum,score(msum,hsum)])

	for row in neutralComparisionTable:
		msum = 0
		nsum = 0
		hsum = 0
		for parameter in row:
			msum += parameter[0]
			nsum += parameter[1]
			hsum += parameter[2]
		dtNeutral.append([msum,nsum,hsum,score(msum,hsum)])

	rankList = []

	def findWhichIsMax(candidateIndex1, candidateIndex2, theList):
		if theList == 1:
			for priorityValue in priorityOrder:
				candidate1Score = score(pessimisticTable[candidateIndex1][priorityValue][0],pessimisticTable[candidateIndex1][priorityValue][2])
				candidate2Score = score(pessimisticTable[candidateIndex2][priorityValue][0],pessimisticTable[candidateIndex2][priorityValue][2])
				if candidate1Score>candidate2Score:
					higher = candidateIndex1
					break
				elif candidate2Score>candidate1Score:
					higher = candidateIndex2
					break
				else:
					continue
			return higher
		elif theList == 2:
			for priorityValue in priorityOrder:
				candidate1Score = score(optimisticTable[candidateIndex1][priorityValue][0],optimisticTable[candidateIndex1][priorityValue][2])
				candidate2Score = score(optimisticTable[candidateIndex2][priorityValue][0],optimisticTable[candidateIndex2][priorityValue][2])
				if candidate1Score>candidate2Score:
					higher = candidateIndex1
					break
				elif candidate2Score>candidate1Score:
					higher = candidateIndex2
					break
				else:
					continue
			return higher
		else:
			for priorityValue in priorityOrder:
				candidate1Score = score(neutralTable[candidateIndex1][priorityValue][0],neutralTable[candidateIndex1][priorityValue][2])
				candidate2Score = score(neutralTable[candidateIndex2][priorityValue][0],neutralTable[candidateIndex2][priorityValue][2])
				if candidate1Score>candidate2Score:
					higher = candidateIndex1
					break
				elif candidate2Score>candidate1Score:
					higher = candidateIndex2
					break
				else:
					continue
			return higher
		return candidateIndex1

	def findRank(givenList,number):
		tempList = [givenList[x][3] for x in xrange(len(givenList))]
		ranks = [-1 for x in xrange(len(tempList))]
		limit = len(tempList)
		i=0
		previousValue = -9999
		previousIndex = -1
		while(i<limit):
			maxi = max(tempList)
			maxiInd = tempList.index(maxi)
			
			if str(maxi) != str(previousValue):
				ranks[maxiInd] = i+1
				tempList[maxiInd] = -9999
				previousValue = maxi
				previousIndex = maxiInd
			else:
				higher = findWhichIsMax(previousIndex,maxiInd,number)
				if previousIndex==higher:
					ranks[previousIndex]=i
					ranks[maxiInd] = i+1
				else:
					ranks[previousIndex] = i+1
					ranks[maxiInd] = i
			tempList[maxiInd] = -9999
			i+=1
		return ranks
	rankList.append(findRank(dtOptimistic,2))
	rankList.append(findRank(dtPessimistic,1))
	rankList.append(findRank(dtNeutral,3))
	return rankList

noOfJudges = 3

judgeRanks = []
for i in xrange(1,noOfJudges+1):
	judgeRanks.append(calculateRankList("testJudge" + str(i)))

newRanksList = []

for judgeRank in judgeRanks:
	for each in judgeRank:
		newRanksList.append(each)

colSumList = []
for i in xrange(len(newRanksList[0])):
	colSum = 0
	for j in xrange(len(newRanksList)):
		colSum += newRanksList[j][i]
	colSumList.append(colSum)

numberOfCandidates = len(colSumList)

normalizedScore = []
for candidateScore in colSumList:
	normalizedScore.append((2.0*(noOfJudges*3.0*numberOfCandidates-candidateScore))/(noOfJudges*3.0*numberOfCandidates*(numberOfCandidates-1)))

print normalizedScore

#------------Calculate rank---------------
normalizedRank = [-1 for x in xrange(len(normalizedScore))]

tempList = list(normalizedScore)
i=0
limit = len(normalizedScore)
while(i<limit):
	maxi = max(tempList)
	maxiInd = tempList.index(maxi)
	normalizedRank[maxiInd] = i+1
	tempList[maxiInd] = -9999
	i+=1

print normalizedRank