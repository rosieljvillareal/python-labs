import filecmp

path = '/home/rose/py_scripts/file-samples/'

print('common_file :', end=' ')
print(filecmp.cmp(path + 'dir1/doe-a-deer.json', path + 'dir2/doe-a-deer.json', shallow=True), end=' ')
print(filecmp.cmp(path + 'dir1/doe-a-deer.json', path + 'dir2/doe-a-deer.json', shallow=False))

print('contents_differ:', end=' ')
print(filecmp.cmp(path + 'dir1/doe-a-deer.json', path + 'dir2/doe-a-deer.yaml', shallow=True), end=' ')
print(filecmp.cmp(path + 'dir1/doe-a-deer.json', path + 'dir2/doe-a-deer.yaml', shallow=False))

print('identical :', end=' ')
print(filecmp.cmp(path + 'dir1/doe-a-deer.json', path + 'dir1/doe-a-deer.json', shallow=True), end=' ')
print(filecmp.cmp(path + 'dir1/doe-a-deer.json', path + 'dir2/doe-a-deer.json', shallow=False))

