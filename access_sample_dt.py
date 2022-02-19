# Try parsing and converting the timestamp from the string in
# access_sample.log into a datetime object
# Put your answer in a script called: access_sample_dt.py
# The script should accept the log file as parameter
# i.e. python access_sample_dt.py access_sample.log
# It should then return and print the extracted datetime object.

import argparse
import re
from datetime import datetime

def convert_to_datetime(fname):
    with open(fname) as f:
        fstring = f.read()
    
    # search for datetime
    pattern = '\d{2}\/[a-zA-Z]+\/\d{4}\:\d{2}\:\d{2}\:\d{2}'

    for o in fstring.split():
        match = re.search(pattern, o)
        if match:
            dt_str = match.group(0)
            # print(f'word: {o}') 
            print(f'type: {type(dt_str)}')
            print(dt_str)
    
    # convert to datetime object
    dt_obj = datetime.strptime(dt_str, '%d/%b/%Y:%H:%M:%S')
    print(f'type: {type(dt_obj)}')
    print(f'datetime object: {dt_obj}')
    return dt_obj

def main(args):
    fname = args.filename
    convert_to_datetime(fname)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='file to parse')
    args = parser.parse_args()
    main(args)


