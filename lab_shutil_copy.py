import os
import shutil

# WRITE PATH HERE
path = "/home/rose/py2_scripts/"

source = path + 'source/'

sourcefile = source + 'sample.txt'

destination = path + 'destination/' 

print("Before copying:")
print("source", os.listdir(source))
print("destination", os.listdir(destination))

dest = shutil.copy(sourcefile, destination)

print("After copying:")
print("source", os.listdir(source))
print("destination", os.listdir(destination))

print("Destination path:", dest)
