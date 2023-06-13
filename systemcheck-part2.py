"""
Project_2_PrintData.py

Prints json file content to the terminal

Monty Albobsairy
"""
import json

JSONFILE = "Cpu_info.json"

def ReadJsonContent():
    try:
        file_ref = open(JSONFILE, 'r')
        dictionary = json.load(file_ref)
        file_ref.close()
    except:
        print("Could not read file")

    return dictionary


def Divider():
    length = range(100)
    for character in length:
        if character % 2 == 0:
            print('~', end='')
        else:
            print('-', end='')
    print()



def WriteComputerName():
    Divider()
    computer_name = dictionary["ComputerName"]
    print("\nComputer Name:\n")
    Divider()
    print(computer_name)

def WriteAccountInfo():
    Divider()
    print("\nAccounts and Groups:\n")
    Divider()
    account_table = dictionary["AccountTable"]
    for account in account_table:
            str_account = str(account)
            accounts_formatted = str_account.replace('[', '').replace(']', '').replace(',', '\n\t').replace("'", "")
            print(accounts_formatted)


def WriteCpuInfo():
    Divider()
    print("\nCpu Information:\n")
    Divider()
    cpu_info = dictionary["CpuInfo"]
    for info in cpu_info:
        print(info)


def WriteServices():
    Divider()
    print("\nAll Running Services:\n")
    Divider()
    all_services = dictionary["AllServices"]
    for service in all_services:
        print(service)

dictionary = ReadJsonContent()
WriteComputerName()
WriteAccountInfo()
WriteCpuInfo()
WriteServices()