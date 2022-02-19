import os
import shutil

# WRITE PATH HERE
path = "/home/rose/py2_scripts/"

source = path + 'source/'

destination = path + 'destination/' 

print("Before moving file:")
print(os.listdir(path))

dest = shutil.move(source, destination)

print("After moving file:")
print(os.listdir(path))

print("Destination path:", dest)
