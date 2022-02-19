import xml.etree.ElementTree as ET
import xmltodict

with open('file-samples/doe-a-deer.xml') as fd:
	doc = xmltodict.parse(fd.read())
	print(doc)
