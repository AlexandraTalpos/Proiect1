# importing the csv module
 import csv
 
 # my data rows as dictionary objects
 mydict =[{'skill': 'Communication', 'grade degree': '10',
 		'name': 'Ana', 'year': '1976'},
 		{'skill': 'Ledearship', 'grade degree': '7',
 		'name': 'Maria', 'year': '2000'},
		{'skill': 'Empathy', 'grade degree': '9',
 		'name': 'Alexandra', 'year': '1988'},
		{'skill': 'Confidence', 'grade degree': '8',
 		'name': 'Andreea', 'year': '1999'}]
 
 
 # field names
 fields = ['name', 'skill', 'year', 'grade degree']
 
 # name of csv file
filename = "P1note.csv" 
 # writing to csv file
 with open(filename, 'w') as csvfile:
	# creating a csv dict writer object
	writer = csv.DictWriter(csvfile, fieldnames = fields)
	
	# writing headers (field names)
 	writer.writeheader()	
	# writing data rows
	writer.writerows(mydict)
	

# name of csv file
filename = "P1note.csv"

# writing to csv file
with open(filename, 'w') as csvfile:
	# creating a csv dict writer object
	writer = csv.DictWriter(csvfile, fieldnames = fields)

	# writing headers (field names)
	writer.writeheader()

	# writing data rows
