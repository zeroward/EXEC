# EXigentECho
## ICS/SCADA Attack Framework
Making Strategic Attacks Easy



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

## Installation
Run setup script to create a virtual environment and install dependencies:
```shell
chmod +x ./setup.sh && setup.sh
```

Run ExigentEcho in your virtual environment:
```shell
source env/bin/activate
chmod +x ./exigent.py
````

##Operation
- Initilize JSON configuration File
- Build Operator Accesses
- Pick DEMO Mode
- Add targets through Save function
- Query targets to verify
- Go to Attack mode
- Agree to usage policy
- Build Operation
- Launch Attack

