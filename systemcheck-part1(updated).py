import socket, os, pwd, grp, json
'''
Systemcheck-part1

a linux system check script with getting hostname and groups and getting cpu information.
also getting services and creating directories and keeping record at a json file

Mohamad, Monty June 11/23
'''


JSONFILE = "Cpu_info.json"


"simple function that gets the hostname of this machine or computer"
def ComputerName():
    return socket.gethostname()


"a function to get names and groups also its being sorted alphabetically"
def GetNamesAndGroups():
    account_records = []
    all_records = pwd.getpwall()
    for account in all_records:
        group_id = account.pw_gid
        default_group_record = grp.getgrgid(group_id)
        account_name = account.pw_name
        default_group_name = default_group_record.gr_name
        all_group_records = grp.getgrall()
        group_list = [default_group_name]
        for group in all_group_records:
            group_member_lists = group.gr_mem
            if account_name in group_member_lists:
                group_list.append(group.gr_name)
        account_records.append([account_name, group_list])
    sorted_table = sorted(account_records, key=lambda record: record[0].lower())
    return sorted_table


"a simple function to get cpu information like cpu architecture or how many cores we have"
def GetCpuInfo():
    try:
        with open("/proc/cpuinfo", 'r') as file_ref:
            data = file_ref.read().splitlines()
    except:
        print("Could not obtain file")

    keywords = ["vendor_id", "model", "model name", "cache"]
    cpu_info_list = []
    cpu_info_formatted = []
    for word in keywords:
        for line in data:
            if word in line:
                cpu_info_list.append(line)
                break
    for keywords in cpu_info_list:
        cpu_info_list = keywords.replace("\t", '')
        cpu_info_formatted.append(cpu_info_list)
    return cpu_info_formatted


'''this function is to check system running services on machine or computer.
at the end it will return us a list active running system services on machine or computer in formatted way '''
def GetServices():
    service_array = []
    service_formatted = []
    all_services = os.popen("systemctl list-units --type=service")
    for service in all_services:
        service_array.append(service)
    for service in service_array:
        service_array = service.replace("\n", '')
        service_formatted.append(service_array)
    return service_formatted


"This part is write information to a javascript object notation file."
def WriteToJson():
    try:
        with open(JSONFILE, 'w') as jsonFileRef:
            json.dump(info_dictionary, jsonFileRef,indent=2)
    except:
        print("Could not write to file")



"This function will create dictionary to have computer name, account table, cpu information, and all servicess in sorted order."
def CreateDictionary():
    dictionary = {"ComputerName": computer_name,
                  "AccountTable": sorted_table,
                  "CpuInfo": cpu_info_formatted,
                  "AllServices": service_array
                  }
    return dictionary


computer_name = ComputerName()
sorted_table = GetNamesAndGroups()
cpu_info_formatted = GetCpuInfo()
service_array = GetServices()

info_dictionary = CreateDictionary()

WriteToJson()
