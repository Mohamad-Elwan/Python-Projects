"""
tripwire.py

Comparing directories and determining modified, added, and removed files

Mohamad Elwan, Monty May 27/23
"""



import os, hashlib, sys

test_folder = "/home/mohamad/test"
trip_wire_record = "trip_wire_record.txt"

#Get files
def GetFiles():
    list_of_files = []
    try:
        list_of_files = os.popen("ls " + test_folder).read().splitlines()
    except:
        sys.exit(1)
    return list_of_files


def HashFile(my_file):
    try:
        my_file = test_folder + "/" + my_file
        with open(my_file, "rb") as file:
            data = file.read()
            file_hash = hashlib.sha256(data).hexdigest()
        return file_hash
    except:
        print("File not found!\n")
        return None


def WriteToFile(list_of_files):
    info_to_write = [test_folder]
    for name in list_of_files:
        my_file = os.path.join(test_folder, name)
        file_hash = HashFile(file_path)
        if file_hash is not None:
            info_to_write.append(name + " " + file_hash)
    try:
        with open(trip_wire_record, 'w') as write_file:
            for name_and_hash in info_to_write:
                write_file.write(name_and_hash + '\n')
    except:
        print("Could not write to file")


def GetRecord():
    try:
        file = open(trip_wire_record, 'r')
        file_record = file.read().splitlines()
        file.close()
    except:
        print("Couldn't get record for ", trip_wire_record)
    return file_record


def CheckForAddedModifiedRemoved():
    files_to_hash = []
    missing_files = []
    modified_files = []
    current_list = GetFiles()
    file_record = GetRecord()
    file_record.pop(0)
    try:
        for name in list_of_files:
            found = False
            for log in file_record:
                split_line = log.split()
                if split_line[0] == name:
                    found = True
                    files_to_hash.append(split_line[0])
                    current_list.remove(split_line[0])
                    old_hash = split_line[1]
                    if old_hash != HashFile(name):
                        modified_files.append(name)
                elif found == False:
                    missing_files.append(split_line[0])
    except:
        print("Could not check the files!")
    return files_to_hash, missing_files, modified_files, current_list

#MAIN
record_path = "/home/mohamad"
file_path = os.path.join(record_path, trip_wire_record)
if os.path.exists(file_path):
    list_of_files = GetFiles()
    missing_files, modified_files, current_list, files_to_hash = CheckForAddedModifiedRemoved()
    print(missing_files, modified_files, files_to_hash)

else:
    list_of_files = GetFiles()
    WriteToFile(list_of_files)
