import json

# Reading JSON content from file
with open('/tmp/file.json', 'r') as f:
	data = json.load(f)
	print(data)

# Writing JSON content to file using dump method
# with open('/tmp/file.json', 'w') as f:
#	json.dump(data, f, sort_keys=True)
