import json
import os
import time
import hashlib
from config import mod_modbustcp


def op_builder(mission_data, path='./config/config.json'):

    # Extensible Operation Builder
    # Only supports ModbusTCP for now
    targets = mission_data['Target']
    i = 0
    valid_targets = []
    selected_targets = []
    for k, v in targets.items():
        if v['protocol']['protocol'] == "modbustcp":
            i += i
            valid_targets.append([k,v])
    print('Target Parser')
    print('Valid Targets')
    for x in valid_targets:
        print(x[0] + " - " + x[1]['ip'])
    print("Select targets to load")
    tgtchoice = input("Input Target Name (c to complete): ")
    while tgtchoice != "c":
        for x in valid_targets:
            if x[0].lower() == tgtchoice.lower():
                selected_targets.append(x)
        tgtchoice = input("Input Target Name: ")
    for x in selected_targets:
        for k, v in x[1]['protocol']['coils'].items():
            #x[1]['protocol']['coils'][k] = input("Coil {}  - True or False: ".format(k))
            x[1]['protocol']['coils'][k] = [] 
            x[1]['protocol']['coils'][k].append(input("Coil {} - True or False: ".format(k)))
            x[1]['protocol']['coils'][k].append(input("Cycle {}? (Y/N): ".format(k)))
        for k, v in x[1]['protocol']['registers'].items():
            x[1]['protocol']['registers'][k] = input("Register {}  - True or False: ".format(k))

    print(selected_targets)

    with open(path, "r") as f:
        data = json.load(f)
        f.close()

    for k, v in data.items():
        if k == "Mission":
            v.update({"EE": selected_targets})

    with open(path, "w+") as f:
        json.dump(data, f, indent=4)
        f.close()


def load_op(mission_data):
    missions = mission_data['Mission']
    targetload = {}
    for x in missions['EE']:
        targetload[x[1]['ip']] = x[1]['protocol']
    mod_modbustcp.attack(targetload)


def opname_parser(mission_data):
    print("Operation: {}".format((mission_data['Configuration']['Header']['Operation']).upper()))


def attack_menu(path='./config/config.json'):
    with open(path, "r") as f:
        mission_data = json.load(f)
        f.close()
    print("[!] Attack Menu Selected")
    print("[!] This script is to be used by AUTHORIZED INDIVIDUALS ONLY")
    print("[!] The creator of this script is not liable for any effects created by unauthorized use")
    consent = input("[!] Are you an authorized user? (Y/N): ")
    if consent.lower() != "y":
        print("Unauthorized Use Detected, Tearing Down")
        exit()
    c = 0
    while c <= 2:
        password = input("[!] Password required to continue: ")
        hash_object = hashlib.sha512(bytes(password, 'utf-8'))
        hex_dig = hash_object.hexdigest()
        #print(hex_dig)
        #if hex_dig.upper() == "E5723FA2590F2017C245C2B660DDC0B27A04A37CE77CC4F794DB7C9762BC49A79B59F8E5AEE7CC492C680DF4B58A146F61FAB7B81CD50EA8DD5AA544068C7DB2":
        if True:
            print("Welcome, Operator")
            opname_parser(mission_data)
            print("[!] Attack Operations Menu [!]")
            print("- [B]uild Operation")
            print("- [C]lear Operation")
            print("- [L]aunch Attack")
            print("- [H]elp")
            print("- EXIT")
            demo_choice = input("> ")
            if demo_choice.lower() == "b":
                op_builder(mission_data)
                with open(path, "r") as f:
                    mission_data = json.load(f)
                    f.close()
            elif demo_choice.lower() == "c":
                pass
                with open(path, "r") as f:
                    mission_data = json.load(f)
                    f.close()
            elif demo_choice.lower() == "l":
                load_op(mission_data)
                with open(path, "r") as f:
                    mission_data = json.load(f)
                    f.close()
            elif demo_choice.lower() == "h":
                print("Build Operation\n    -Develop operation plan")
                print("Save Target\n    -Clear loaded operation**")
                print("Launch Attack\n    -Launch loaded operation")
                print("Exit\n    -Exit Program")
            elif demo_choice.lower() == "exit":
                exit(0)
        else:
            print("Invalid Password")
            c += 1
