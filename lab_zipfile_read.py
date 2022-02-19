import zipfile

path = '/home/rose/py2_scripts/master.zip'
 
with zipfile.ZipFile(path) as file:
    print('\nInfo List')
    print(file.infolist())
    
    print('\nName List')
    print(file.namelist())
