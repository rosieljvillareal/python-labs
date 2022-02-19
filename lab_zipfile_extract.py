import zipfile
import os

path = '/home/rose/py2_scripts/master.zip'
 
with zipfile.ZipFile(path) as file:
    print(f'The dir files are: {os.listdir(os.getcwd())}')
    
    print('\nExtracting...')
    
    file.extractall()
    
    print(f'The dir files are {os.listdir(os.getcwd())}')
