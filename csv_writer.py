import csv
with open('/tmp/file.csv', newline='') as f:
	writer = csv.writer(f)
	writer.writerows(iterable)
		

