# import Modules
from Modules.rw_csv import writeData, readData, getDataSize
from Modules.todoDataClass import todoData
from Modules.consoleCleaner import clear
from math import ceil

# variable declaration
done = False
ment = None

while not done:
    clear()
    if ment:
        print("[" + ment + "]")
        ment = None
    print("This document currently contains %d pieces of information." %
          getDataSize(), """
1. Write todo.
2. Load all todo lists.
3. Get information about a specific todo.
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
            while True:
                data = readData()
                if not data:
                    print("Data is not definded")
                    break
                datas = []
                page = 1
                pages = ceil(len(data) / 5)
                print("This page is %d" % (page))
                print("=" * 53)
                print(format("index", "^5")," | ",format("topic", "^20")," | ",format("date", "^10")," | ",format("succeeded", "^9"), sep="")
                print("=" * 53)
                pageData = next((i for i in data if page <= int(i['index']) or page * 5 >= int(i['index']) ), None)
                for i in data:
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
        case "e":
            break
        case _:
            ment = "It's not the right choice."
