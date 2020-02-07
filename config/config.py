import json
import datetime
import os
from prettytable import PrettyTable


def build_config(path):
    print("Building Configuration File...")
    file_header = {}
    tgt_placeholder = {}
    mission_profile_holder = {}

    # Hardcoded Version
    ver = "DEV ALPHA .1"

    # Init time
    start_time = datetime.datetime.utcnow().strftime("%d-%b-%Y (%H:%M:%S.%f)")

    # User entries
    file_header['Platform Version'] = ver
    file_header['username'] = input("Enter Your username: ")
    file_header['Operation'] = input("Input Operation Name: ")
    file_header['UTC Start Time'] = start_time

    file_contents = {"Header": file_header}
    config_build = {"Configuration": file_contents, "Target": tgt_placeholder, "Mission": mission_profile_holder}

    with open(path, "w") as f:
        json.dump(config_build, f, indent=4)
        f.close()


def parse_header(data):
    print("Current Mission Data")
    print("EE Config Version: {}".format(data['Configuration']['Header']['Platform Version']))
    print("User: {}".format((data['Configuration']['Header']['username']).upper()))
    print("Operation: {}".format((data['Configuration']['Header']['Operation']).upper()))
    print("Operation Start Time {}".format(data['Configuration']['Header']['UTC Start Time']))
    return 0


def parse_saves(path='./config/config.json'):
    x = PrettyTable()
    x.field_names = ["Target Name", "Type", "IP Address", "Protocol"]
    with open(path, "r") as f:
        data = json.load(f)
    tgts = data['Target']
    for k, v in tgts.items():
        row = [k]
        for e, c in v.items():
            row.append(c)
        x.add_row(row)
    print(x)


def target_save(path='./config/config.json'):
    tgtname = input("Target Name: ")
    coils = {}
    registers = {}
    coregs = {}
    print("Available Target Types")
    print("""
    - HMI
    - PLC
    - RTU
    - Client
    - Misc
    """)
    targetdata = {'type': input("Pick Type: "),
                  'ip': input("IP address:"),
                  }
    protocol = input("Protocol Used:")
    if targetdata['type'].lower() == 'plc' and protocol == 'modbustcp':
        coil = input("coil location (c to complete): ")
        coregs['protocol'] = protocol
        while coil.lower() != "c":
            if coil.isdigit():
                coils[coil] = ""
                coil = input("coil location (c to complete): ")
            else:
                print("Invalid Response, use c to exit")
                coil = input("coil location (c to complete): ")
        coregs['coils'] = coils
        reg = input("register location (c to complete): ")
        while reg.lower() != "c":
            if reg.isdigit():
                registers[reg] = ""
                reg = input("register location (c to complete): ")
            else:
                print("Invalid Response, use c to exit")
                reg = input("register location (c to complete): ")
        coregs['registers'] = registers
    else:
        coregs['protocol'] = protocol

    targetdata['protocol'] = coregs

    with open(path, "r") as f:
        data = json.load(f)
        f.close()

    # Parse out existing Targets
    for k, v in data.items():
        if k == "Target":
            v.update({tgtname: targetdata})

    with open(path, "w+") as f:
        json.dump(data, f, indent=4)
        f.close()


def config_load(path='./config/config.json'):
    try:
        with open(path, "r") as f:
            try:
                data = json.load(f)
                print("Valid Configuration File Loaded - Parsing!\n")
                parse_header(data)
            except ValueError:
                print("Invalid JSON File Loaded - Advise deletion and rebuild")
    except IOError:
        print('Unable to find config file at {}'.format(path))
        check = input("Input different filename? [Y/N]: ")
        print(check.lower())
        if check.lower() == "n":
            build_config(path)
            print("Configuration File Built! Parsing for sanity check!\n")
            config_load(path)
        elif check.lower() == "y":
            path = input("Input file path: ")
            try:
                with open(path, "r") as f:
                    f.close()
                config_load(path)
            except FileNotFoundError:
                print("Invalid File Name, building new config at path")
                build_config(path)
    return 0


def module_load(path="./config/"):
    modlist = {}
    for f in os.listdir(path):
        if f.startswith("mod_") and f.endswith(".py") and not f.endswith(".pyc"):
            with open(path + f, "r") as m:
                for x in m.readlines():
                    if x.startswith("SHA256"):
                        modlist[f] = x
    for k, v in modlist.items():
        print("Modules Loaded:")
        print(k)
    print("\n")
