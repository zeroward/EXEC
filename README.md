# EXigentECho
### ICS/SCADA Attack Framework
### Making Strategic Attacks Easy



                                                    _.-^^---....,,--       
                                                 --                  --_  
                                               <                        >)
                                               |                         | 
                                                \._                   _./  
                                                   ```--. . , ; .--'''       
                                                         | |   |             
                                                      .-=||  | |=-.   
                                                      `-=#$%&%$#=-'   
                                                         | ;  :|     
                                                _____.,-#%&$@%#&#~,._____
                                               

## Capabilities
EXEC is capable of creating and storing mission profiles to perform ICS/SCADA attacks. This does not automate everything, rather it gives you a pretty interface to leverage pymodbus through.
### Supported Protocol
ModbusTCP

## Development Progress
### 1.0 Release Milestones
- [x] Modbus Module Integration
- [ ] DNP3 Module Integration
- [ ] Config import/export
### 2.0 Release Milestones
- [ ] Web Interface
- [ ] Collaboration
### Future Goals
- [ ] BACNet Module Integration
- [ ] Ethernet/IP Module Integration
- [ ] Profinet Module Integration

Installation
-----

```shell
python3 runfirst.py
python3 exigent.py
````

### Required Modules (installed by runfirst.py):
- PrettyTable
- Pymodbus

Supported Protocols
-----
ModbusTCP

Operation
-----

-> initilize JSON configuration File<br>
-> Build Operator Accesses<br>
-> Pick DEMO Mode<br>
-> Add targets through Save function<br>
-> Query targets to verify<br>
-> Go to Attack mode<br>
-> Agree to usage policy<br>
-> Build Operation<br>
-> Launch Attack

