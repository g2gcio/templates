import pandas as pd
mydata = pd.read_csv('data.txt', delimiter=',', dtype="S8,S5", names=["f1","f2"])
print "1=================================="
print mydata
print "2=================================="	
