import datetime
from config import config
import attacks

version = ".1"
current_time = datetime.datetime.utcnow()


def demo():
    print("Demo Mode Enabled - For Bricks In The Loop Attacks Only")
    print("- [A]ttack")
    print("- [S]ave Target")
    print("- [Q]uery Saved Targets")
    print("- [H]elp")
    print("- EXIT")
    while True:
        demo_choice = input("> ")
        if demo_choice.lower() == "a":
            attacks.attack_menu()
        elif demo_choice.lower() == "s":
            config.target_save()
        elif demo_choice.lower() == "q":
            config.parse_saves()
        elif demo_choice.lower() == "h":
            print("Attack\n    -Enter attack mode, enabling a mission to be built and executed")
            print("Save Target\n    -Enable management of the target database **MUST BE POPULATED PRIOR TO MISSION "
                  "EXECUTION**")
            print("Query Saved Targets\n    -Query Target Database")
            print("Exit\n    -Exit Program")
        elif demo_choice.lower() == "exit":
            exit(0)


def menu():
    print("EXIGENT ECHO MAIN MENU")
    print("OPERATION MODES")
    print("- GUIDED MODE [DEMO]")
    print("- ATTACK MODE [ATTACK]")
    print("- EXIT [EXIT]")
    while True:
        choice = input("Select Program Operation Mode > ")
        if choice.lower() == "demo":
            demo()
        elif choice.lower() == "attack":
            attack()
        elif choice.lower() == "exit":
            print("Session Teardown Initiated")
            print("Teardown Complete!")
            exit()
        else:
            print("Invalid Decision")


def main():
    print("="*20)
    print("EXIGENTECHO Attack Platform \nFOR EXERCISE USE ONLY")
    print("="*20+"\n")
    print("Version {}".format(version))
    print("Initialization time is {} GMT\n".format(current_time))
    config.config_load()
    config.module_load()
    menu()


if __name__ == "__main__":
    main()



