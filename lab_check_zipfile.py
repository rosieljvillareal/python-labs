import zipfile

filelist = ['destination', 'source', 'lab_check_zipfile.py', 'master.zip',
            'doesnotexist.zip']

# also returns False if file does not exist
for filename in filelist:
    print(filename, zipfile.is_zipfile(filename))
