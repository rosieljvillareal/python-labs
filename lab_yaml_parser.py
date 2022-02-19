import yaml

with open('file-samples/doe-a-deer.yaml', 'r', newline='') as f:
	try:
		print(yaml.load(f))
	except yaml.YAMLError as ymlexcp:
		print(ymlexcp)

