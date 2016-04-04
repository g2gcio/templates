import csv
import numpy as np
from itertools import ifilterfalse
from itertools import chain
from operator import itemgetter, attrgetter, methodcaller

array = []
array1 = []

with open('data.txt', 'r') as csvfile:
	filtered_csvfile = ifilterfalse(lambda line: line.startswith('\n'), csvfile)
	reader = csv.reader(filtered_csvfile, delimiter=',')
	for row in reader:
		field = row[0].split("-")
		field = map(int,field)
		r=row[1].replace(" ","")
		field.append(int(r[0]))
		field.append(int(r[1]))
		field.append(int(r[2]))
		field.append(int(r[3]))
		array.append(row)
		array1.append(field)
#		print field
#print array1
print "=================================="
array2 = sorted(array1, key=lambda x: x[3])
print array1
ind = np.lexsort(array1[:,1],array1[:,0])
print array2[ind]
#for i in array3:
#	print i
#print "=================================="
#array2 = sorted(array1, key=lambda x: x[1])
#for i in array2:
#	print i
	
	
