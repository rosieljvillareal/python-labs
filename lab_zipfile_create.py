import zipfile

print('creating archive')
zf = zipfile.ZipFile('sample.zip', mode='w')
try:
    print('adding README.txt')
    zf.write('README.txt')
finally:
    print('closing')
    zf.close()
