import os
import filecmp
import csv
import itertools
import re

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys will come from the first row in the data.

#Note: The column headings will not change from the
#test cases below, but the the data itself will
#change (contents and size) in the different test
#cases.

	#Your code here:

	with open(file, 'r') as mycsv:
		reader=csv.DictReader(mycsv)

		lst=[]
		#header=next(reader)

		for i in reader:
			#print(i)
			d={}
			d['First']=i['First']
			d['Last']=i['Last']
			d['Email']=i['Email']
			d['Class']=i['Class']
			d['DOB']=i['DOB']
			lst.append(d.copy())
		#print(lst)
		return(lst)



#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

#Sort based on key/column
def mySort(data,col):
	funsort=sorted(data,key=lambda x:x[col])
	return (funsort[0]["First"] +' ' +funsort[0]["Last"] )
	#return ''







	pass
#Create a histogram
def classSizes(data):
# Input: list of dictionaries
	counts={}
	for student in data:
		countsget=student.get('Class')

		if countsget not in counts:
			counts[countsget] =1
		else:
			counts[countsget]+=1
	x=counts.items()
	t=sorted(x,key=lambda x:(-x[1],x[0]))
	return t
#




	pass
#
#
#
def findDay(a):
	Bday={}
	for person in a:
		getBday=person.get('DOB')
		y=re.findall('^[0-9]+/([0-9]+)/0-9+',getBday)





	print(y)


# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	pass


# Find the average age (rounded) of the Students
def findAge(a):
	#Your code here:
	# dt.date.today()
	# pass

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
# def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	pass



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)

	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()
