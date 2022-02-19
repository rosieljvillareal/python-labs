import csv

fname = input('Enter filename to process: ')

with open(fname, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    fieldnames = reader.fieldnames
    
    newfile = open('clean_products.csv', 'w', newline='') 
    writer = csv.DictWriter(newfile, fieldnames=fieldnames)
    writer.writeheader()
	
    for row in reader:		
        if len(row['Categories']) != 0:
            writer.writerow(row)
	
    print('Output file written in clean_products.csv')
