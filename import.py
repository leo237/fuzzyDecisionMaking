import csv 

parameters = []
fuzzySet = []
rows = []

counter = 0
with open('dataInput.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		if counter == 0:
			parameters = list(row)
		else:
			temp = []
			for each in row:
				temp.append(float(each))
			fuzzySet.append(temp)
		counter+=1

numberOfParameters = len(parameters)
numberOfHouses = len(fuzzySet)

for i in xrange(1,numberOfHouses+1):
	s = 'h'+str(i)
	rows.append(s)

print parameters
print fuzzySet
print rows