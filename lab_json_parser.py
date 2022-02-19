import json

# Reading JSON content from file
with open('file-samples/doe-a-deer.json') as f:
	data = json.load(f)
	print(data)

