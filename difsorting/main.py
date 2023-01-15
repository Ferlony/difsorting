import sort_datatime
import rename_by_hash
from sortingdep import conformation


""" 
test

/home/theuser/Pictures/

"""


def menu():
    while True:
        print("Choose action\n"
              "'1' Files sorting\n"
              "'2' Rename files by hash\n"
              "'3' Rename files by hash and sort them by modification time\n"
              "'0' Close program")
        inp = input()
        if inp == "1":
            while True:
                print("Choose sorting\n"
                      "'1' By modification time\n"
                      "'0' Back")
                sort_inp = input()
                if sort_inp == "1":
                    print("Enter files folder location")
                    path = input()
                    print("Chosen path:\n", path)
                    if conformation.conformation():
                        sort_datatime.SorterDataTime(path).platform_worker()
                elif sort_inp == "0":
                    break
                else:
                    print("Wrong input")

        elif inp == "2":
            print("Enter files folder location")
            path = input()
            print("Chosen path:\n", path)
            if conformation.conformation():
                print(rename_by_hash.RenamerByHash(path).platform_worker())

        elif inp == "3":
            print("Enter files folder location")
            path = input()
            print("Chosen path:\n", path)
            if conformation.conformation():
                sort_datatime.SorterDataTime(rename_by_hash.RenamerByHash(path).platform_worker()).platform_worker()

        elif inp == "0":
            return
        else:
            print("Wrong input")


def main():
    menu()
    return 0


if __name__ == "__main__":
    main()
