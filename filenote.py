#!bin/python

import csv
import os
import sys
import subprocess
import datetime
import time

CSV_FILE_NAME = 'note.csv'
csv_dict = {}
prompt_dict = {}
files_list = []
ignore_list = [CSV_FILE_NAME,
               'filenote.py',
               'README.md',
               '.gitignore',
               '.git']
ignore_list = ignore_list + [c + "~" for c in ignore_list]

if __name__ == "__main__":
    dir = str(sys.argv[1])
    dir_path = os.path.abspath(dir)
    def abspath(file_name):
        return dir_path + "/" + CSV_FILE_NAME
    
    csv_path = abspath(CSV_FILE_NAME)
    # check if filenote.csv exists in directory
    if os.path.isfile(csv_path):
        pass
    else:
        # if not exist, create the file        
        args = ['touch', csv_path]
        subprocess.Popen(args)
        time.sleep(0.5)
    
    # if exists, make sure all the files are in the CSV (additive)
    with open(csv_path, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            if len(row) == 3:
                csv_dict[row[0]] = (str(row[1]), str(row[2]))

    # if entry exist but file is gone, mark as deleted
    for (k,v) in csv_dict.items():
        if not os.path.isfile(abspath(k)):
            tup = file_dict[k]
            csv_dict[k] = (tup[0], tup[1] + " (Deleted)")
    # everything else in file_dict is in the csv and exists -- ignore
    # whats left: all the files
    files_list = os.listdir(dir_path)
    for f in files_list:
        if f in csv_dict.keys():
            tup = csv_dict[f]
            if tup[1] == "":
                prompt_dict[f] = ("","")
            else:
                pass
        elif f not in ignore_list:
            prompt_dict[f] = ("","")
    print ignore_list
    write_dict = csv_dict
    for (k,v) in prompt_dict.items():
        print str((k,v))
        now = datetime.datetime.now().strftime('%Y%m%d')
        ans=raw_input("Note for " + k + ": ")
        write_dict[k] = (now, ans)

    if len(write_dict) > 0:
        with open(csv_path, 'wb') as csvfile:
            csvfile.write('file,date,note\n')
            for (k,v) in write_dict.items():
                csvfile.write(",".join([k,v[0],v[1]]))
                csvfile.write('\n')
    # build a dictionary of all the files that need to be labeled
    # ones that don't exist in file_dict or have a blank note
    # iterate through dictionary
    
    # prompt files one by one
    # if prompt is empty, create an empty entry
    # if prompt is not empty, write to csv file
