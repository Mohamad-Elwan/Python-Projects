import os, hashlib, sys

'''
tripwire.py

Creating a record for files in a directory and running it through a hash algorithm.
Then checking the record to see if files have been removed added or modified in any way.
This is by using the command line.

Mohamad Elwan, Monty May 28/23

'''

test_folder = "/home/monty/PycharmProjects/CPRG217/test_folder"
trip_wire_record = "trip_wire_record.txt"

"""Simple function that gets the files that are in the test_folder. It reads the folder then splits
the lines to get all the files needed. If it cant get any files or the directory doesn't
exist it will just exit. It then returns the files with the variable list_of_files."""


def GetFiles():
    try:
        list_of_files = os.popen("ls " + test_folder).read().splitlines()
    except:
        sys.exit(1)
    return list_of_files


"""A function to run the files in the test_folder through a hash algorithm by reading the bytes.
Uses the with statement so that you don't have to close the file after. Uses the hashlib
to get the hash algorith, runs it through the files and returns it. If it doesn't work
since we have added a try except it will tell you it didn't work and return nothing so that
it doesn't give us an error later on."""


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


"""The function that writes the record to a file. It gets the information it needs from the 
test_folder then checks every item in list_of_files and adds it to the list of info but it 
runs it through the hash function first to add both the filename and the hash after.
It will then use a try except block to write it to the record. It will run it through
a for loop to write all files and their hashes into the record. It also uses a with statement
as well."""


def WriteToFile():
    info_to_write = [test_folder]
    try:
        for name in list_of_files:
            file_hash = HashFile(name)
            info_to_write.append(name + " " + file_hash)
            with open(trip_wire_record, 'w') as write_file:
                for name_and_hash in info_to_write:
                    write_file.write(name_and_hash + '\n')
    except:
        print("Could not write to file")
    return


"""A function that obtains the trip_wire_record created. It uses a try except for error handling and uses the with statement
so you don't have to close the file after. It reads the file and splits the lines in the file and removes the path that is
at index 0. Then it returns the file record."""


def GetRecord():
    try:
        with open(trip_wire_record, 'r') as file:
            file_record = file.read().splitlines()
            file_record.pop(0)
    except:
        print("Couldn't get record for ", trip_wire_record)
    return file_record


"""This function checks the files one by one to see if they have been removed added or modified in any way. It works 
by listing the files to hash as an empty list that will be populated later. Same as the missing files list and 
modified files list. It also creates a dictionary to more easily grab the hash value in the file record instead of 
using a list for it. Then it will run a for loop for everything in file_record so it can check through it and it 
splits the name and hash value. Once it has splitted them using the space between them it assigns the file variable 
to index 0 in the splitted lines of the record. Then it adds it into the dictionary, the file name next to its hash 
value. It will then check if the file is in the current list of files and if it is it will add it to files_to_hash 
and remove it from the current list so that we know we need to check if its modified later and so that at the end we 
know which files have been added. Else it will append it to missing files. Another for loop is used to check if the 
files have been modified. If the file is in our dictionary then it will grab its hash from the dictionary and create 
the new hash for the file. If they are not equal it will append it to modified files else it will append it to files 
to hash. It returns files_to_hash, missing-files, current_list and modified files. The current list at this point 
will be the added files."""


def CheckForMissingAddedModified():
    files_to_hash = []
    missing_files = []
    modified_files = []

    file_record_dict = {}

    for record in file_record:
        split_line = record.split()
        file = split_line[0]
        file_record_dict[file] = split_line[1]
        if file in current_list:
            files_to_hash.append(file)
            current_list.remove(file)
        else:
            missing_files.append(file)

    for file in list_of_files:
        if file in file_record_dict:
            old_hash = file_record_dict[file]
            new_hash = HashFile(file)

            if old_hash != new_hash:
                modified_files.append(file)
        else:
            files_to_hash.append(file)
    return files_to_hash, missing_files, current_list, modified_files


"""
This is our main. It uses sys.argv and just checks if the c argument is used. if it is then it will create the record
and if not it will compare the record to see if theres added, removed or modified files in the directory specified.
"""
if 'c' in sys.argv:
    list_of_files = GetFiles()
    WriteToFile()
    print("Record Created")
else:
    file_record = GetRecord()
    list_of_files = GetFiles()
    current_list = GetFiles()
    files_to_hash, missing_files, added_files, modified_files = CheckForMissingAddedModified()
    print(
        "Modified Files: " + str(modified_files) + " \nMissing Files: " + str(missing_files) + "\nAdded Files: " + str(
            added_files))
