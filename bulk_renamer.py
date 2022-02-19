# Python Exercise 6
# Bulk renamer tool for renaming files in a target directory that match a file pattern

# Import libraries
import sys
import argparse
from pathlib import Path
import re
import shutil
import logging
import filecmp


# Note: Catch possible errors & add appropriate logs  

"""
What if new name for target file already exists in directory?

Case 1: Rename 'file0.png' -> 'file0.png' i.e. no renaming needs to be done 
DO: Skip renaming & just log message

Case 2: Rename 'file2.png' -> 'file0.png' but 'file0.png' w/ DIFFERENT content already exists in target_dir' 
DO: Change new filename for 'file2.png', keep incrementing counter by 1 until new filename is unique 

Case 3: Rename 'file2.png' -> 'file0.png' but 'file0.png' w/ SAME content already exists in 'target_dir'
i.e. 'file2.png' & 'file0.png' are copies of each other
DO: Change new filename for 'file2.png', keep incrementing counter by 1 until new filename is unique 
"""

def get_files(target_dir, file_pattern=None):
    """Returns a list of files in the target_dir that contain file_pattern
    
    Parameters
    -----------
    target_dir: (str) The directory where the file to be renamed resides
    file_pattern: (str) The regex that will be used to filter for files in the target directory
    
    Returns
    -----------
    to_rename_list: (list) A list of filenames in the target directory that matched the file pattern
    """
    try:
        target_dirlist = list(Path(target_dir).iterdir())
        fname_dirlist = [Path(fname).name for fname in target_dirlist]
            
        to_rename_list = [fname for fname in fname_dirlist if re.search(file_pattern, str(fname))]
        to_rename_list.sort()
    
    except FileNotFoundError as e:
        logging.error(f'{e}, check the name of your target directory')
        sys.exit(1)
            
    return to_rename_list

 
def have_same_content(file1, file2):
    """Check if file1 has same content as file2 
    
    Parameters
    -----------
    file1: (Path) The filepath of one file
    file2: (Path) The filepath of another file
    
    Returns
    -----------
    (bool) 1 if the two files have the same content, 0 otherwise
    """
    if filecmp.cmp(file1, file2, shallow=False):
        logging.warning(f'Files "{file1}" and "{file2}" have the same content.')
        return 1
    
    else:
        logging.warning(f'New name for file "{file1}" matches an existing but different file "{file2}".')
        return 0

def copy_or_rename(old_fname, new_fname, copy_flag):
    """Copy from old_fname to new_fname if there's a copy_flag, otherwise just rename
    
    Parameters
    -----------
    old_fname: (Path) The old filepath (source) of the target file
    new_fname: (Path) The new filepath (destination) for the target file
    copy_flag: (bool) A flag that when True, copies instead of renames the file
    """
    
    if copy_flag: # Copy file
        shutil.copy(old_fname, new_fname)
        logging.info(f'Copied {old_fname} -> {new_fname}')
        
    else: # Rename file
        shutil.move(old_fname, new_fname)    
        logging.info(f'Renamed {old_fname} -> {new_fname}')

def create_new_name(target_dir, new_name, sfx, counter):
    """Update counter & create new filename if an already existing file in target_dir has same name
    
    Parameters
    -----------
    target_dir: (str) The directory where the file to be renamed resides
    new_name: (str) The file name pattern which will be used to rename the target file
    sfx: (str) The file suffix of the target file, e.g. '.jpg', '.png'
    counter: (int) A number for renaming multiple target files differently
    
    Returns
    -----------
    new_fname: (Path) The updated filepath name to use for renaming target file
    counter: (int) An updated counter
    """

    new_fname = Path(target_dir).joinpath(new_name + str(counter) + sfx)

    while Path(new_fname).is_file():
        counter += 1
        new_fname = Path(target_dir).joinpath(new_name + str(counter) + sfx)    
        logging.info(f'Created new name "{new_fname}" for file')
        
    return new_fname, counter

def rename_file(target_dir, file_path, new_name, copy_flag, counter=None):
    """Rename file_path in target_dir given new_name, optionally
    include counter and copy, instead of renaming, if there's a copy_flag
    
    Parameters
    -----------
    target_dir: (str) The directory where the file to be renamed resides
    file_path: (str) The name of the file to be renamed
    new_name: (str) The file name pattern which will be used to rename the target file
    copy_flag: (bool) A flag that when True, copies instead of renames the file
    counter: (int) A number for renaming multiple target files differently
    """

    old_fname = Path(target_dir).joinpath(file_path)
    sfx = old_fname.suffix
    new_fname = Path(target_dir).joinpath(new_name + str(counter) + sfx)
    
    if Path(new_fname).is_file(): 
    # Check if new name for file matches name of existing file in target_dir

        if have_same_content(old_fname, new_fname) and old_fname == new_fname: 
            # Case 1: Skip renaming
            logging.warning(f'Skipped renaming target file {old_fname} to the same file name')
        
        else: 
            # Case 2 or 3: Keep incrementing counter if file with same name already exists until unique name is created 
            new_fname, counter = create_new_name(target_dir, new_name, sfx, counter)
            # breakpoint()
            
            # Copy or rename file with modified new_fname
            copy_or_rename(old_fname, new_fname, copy_flag)
    
    else:
        copy_or_rename(old_fname, new_fname, copy_flag)
        

def bulk_rename_files(new_name, target_dir, file_pattern, copy_flag):
    """Rename or copy files in target_dir that match file_pattern 
    to new_name with an auto-incremented counter
    
    Parameters
    -----------
    new_name: (str) The file name pattern which will be used to rename the target file
    target_dir: (str) The directory where the file to be renamed resides
    file_pattern: (str) The regex that will be used to filter for files in the target directory
    copy_flag: (bool) A flag that when True, copies instead of renames the file
    """
    to_rename_list = get_files(args.target_dir, args.file_pattern)
    
    if len(to_rename_list) == 0:
        logging.info(f'No files were found to match "{file_pattern}"')
        sys.exit(1)
        
    counter = 0
    
    for f in to_rename_list:
        rename_file(target_dir, f, new_name, copy_flag, counter=counter)
        counter += 1


def main(args):
    try:
        logging.basicConfig(level=args.log_level,
            format='[%(asctime)s] %(levelname)s %(module)s %(lineno)d - %(message)s')
        bulk_rename_files(args.new_name, args.target_dir, args.file_pattern, args.copy)
            
    except ValueError as e:
        logging.error(f'{e}, choose a valid level from [DEBUG, INFO, WARNING, ERROR, CRITICAL]')
        sys.exit(1)
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('new_name',
        help='The file name pattern which will be used to rename the target files.')
    parser.add_argument('file_pattern',
        help='The regex that will be used to filter for files in the target directory.')
    parser.add_argument('target_dir',
        help='The directory where the files to be renamed reside.')
    parser.add_argument('--log_level', '-L',
        help='Set the log level',
        default='INFO')
    parser.add_argument('--copy', '-C',
        help='Add this flag to copy file instead of renaming it',
        action='store_true',
        default=False)
        
    args = parser.parse_args()
    main(args)

