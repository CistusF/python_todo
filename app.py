# import Modules
from Modules.rw_csv import writeData, readData, getDataSize, delData
from Modules.todoDataClass import todoData
from Modules.consoleCleaner import clear
from math import ceil

# variable declaration
ment = None

while True:
    clear()
    if ment:
        print("[" + ment + "]")
        ment = None
    print("This document currently contains %d pieces of information." %
          getDataSize(), """
1. Write todo.
2. Load all todo lists.
3. Get information about a specific todo.
4. Clear specific todo information.
5. Clear todo list.
e. Exit
""", sep="")

    choice = input("Please select the option you wish to proceed with from the options above. : ")
    clear()
    match(choice.lower()):
        case "1":
            while True:
                topic = input("Please enter the topic of todo you want to enter. : ")
                if not topic:
                    print("> topic can't be None")
                    continue
                description = input("Please enter the description of todo you want to enter. : ")
                writeData(todoData(topic, description) if description else todoData(topic))
                ment = "topic %s is successfully added to the todo list" % topic
                break

        case "2":
            page = 1
            while True:
                data = readData()
                if not data:
                    ment = "Data is not definded"
                    break
                datas = []
                pages = ceil(len(data) / 5)
                print("This page is %d" % (page))
                print("=" * 53)
                print(format("index", "^5")," | ",format("topic", "^20")," | ",format("date", "^10")," | ",format("succeeded", "^9"), sep="")
                print("=" * 53)
                for i in data:
                    if (page - 1) * 5 < int(i['index']) and (page-1) * 5 + 5 >= int(i['index']):
                        datas.append(i)
                for i in datas:
                    print(format(i["index"], "^5")," | ",format(i["topic"] if len(i["topic"]) < 20 else i["topic"][:18] + "..", "^20")," | ",format(i["date"], "^10")," | ",format(i["succeeded"], "^9"), sep="")
                choice = input("Please enter page number(or n) : ")
                try:
                    if choice.lower() == "n": 
                        break
                    else:
                        choice = int(choice)
                        if 0 > choice or choice > pages:
                            print("Invalid page number.")
                        else:
                            clear()
                            page = choice
                except:
                    print("You entered incorrect information.")

        case "3":
            while True:
                choice = input("Please enter index number(or n) : ")
                data = readData(choice)
                if choice.lower() == "n":
                    break
                elif not data:
                    print("Invaild index")
                else:
                    clear()
                    for i in data:
                        print(format(i,"<11"), ": ", data[i])

        case "4":
            while True:
                choice = input("Please enter index number(or n) : ")
                data = readData(choice)
                if choice.lower() == "n":
                    break
                elif not data:
                    print("Invaild index")
                else:
                    clear()
                    for i in data:
                        print(format(i,"<11"), ": ", data[i])
                    num = choice
                    print("\n\nAre you sure to delete the above information?")
                    while True:
                        choice = input("Y/N : ").lower()
                        if choice == "y":
                            delData(num)
                            print("Successfully deleted")
                            break
                        elif choice == "n":
                            print("Cancelled")
                            break
                        else:
                            print("Wrong choice")

        case "5":
            choice = input("Are you sure? : (Y/N) : ").lower()
            if choice == "y":
                delData()
                ment = "Successfully deleted all data"
            else:
                ment = "Cancelled"

        case "e":
            break

        case _:
            ment = "It's not the right choice."
