import csv
with open('/tmp/file.csv', newline='') as f:
	reader = csv.reader(f)
	for row in reader:
		print(row)
		

