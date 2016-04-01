import csv
array = []
array1 = []
with open('20160330.txt', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
#		print row[0], row[1]
		field = row[0].split("-")
		field.append(row[1])
		array.append(row)
		array1.append(field)
		print field
with open('20160327.txt', 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
#		print row[0], row[1]
		field = row[0].split("-")
		field.append(row[1])
		array.append(row)
		array1.append(field)
		print field
print array
print array1
