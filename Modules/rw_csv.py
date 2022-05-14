# import Module
import csv

# Handle import for test
if __name__ == '__main__':
    from todoDataClass import todoData
else:
    from Modules.todoDataClass import todoData

# functions declaration
def writeData(todoData: todoData):
    '''Add data to csv file.'''
    todoData = todoData.__dict__
    todoDatas = readData()
    with open('./todo.csv', 'w', newline='') as csvfile:
        fieldnames = ['index', 'date', 'topic', 'description', 'succeeded']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        count = 1
        if todoDatas:
            for i in todoDatas:
                writer.writerow({'index': count, 'date': i["date"], 'topic': i["topic"],
                                'description': i["description"], 'succeeded': i["succeeded"]})
                count += 1
        writer.writerow({'index': count, 'date': todoData["date"], 'topic': todoData["topic"],
                        'description': todoData["description"], 'succeeded': todoData["succeeded"]})


def readData(index=None):
    with open('./todo.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        if not index:
            datas = []
            for i in reader: datas.append(i)
            return datas 
        else:
            data = next((i for i in reader if i['index'] == str(index)), None)
            return data


def getDataSize():
    with open('./todo.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        return sum(1 for i in reader) - 1


# Test Code
if __name__ == '__main__':
    # print(getDataSize())
    # readData(1)
    data = todoData("Test", "Write Data")
    writeData(data)
