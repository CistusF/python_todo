# import Module
import csv

# Handle import for test
if __name__ == '__main__':
    from todoDataClass import todoData
else:
    from Modules.todoDataClass import todoData

# functions declaration
def writeData(todoData: todoData | None):
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


def readData(index: int | None = None):
    '''Return todo data'''
    with open('./todo.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        if not index:
            datas = []
            for i in reader: datas.append(i)
            return datas 
        else:
            data = next((i for i in reader if i['index'] == str(index)), None)
            return data

def delData(index: int=None):
    '''Del data from csv file.'''
    if not index:
        with open('./todo.csv', 'w', newline='') as csvfile:
            fieldnames = ['index', 'date', 'topic', 'description', 'succeeded']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
        pass
    todoDatas = readData()
    with open('./todo.csv', 'w', newline='') as csvfile:
        fieldnames = ['index', 'date', 'topic', 'description', 'succeeded']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        count = 1
        if todoDatas:
            for i in todoDatas:
                if i["index"] == str(index):
                    print(i)
                    continue
                writer.writerow({'index': count, 'date': i["date"], 'topic': i["topic"],
                                'description': i["description"], 'succeeded': i["succeeded"]})
                count += 1

def getDataSize():
    '''Return todo data's size'''
    with open('./todo.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        return sum(1 for i in reader) - 1


# Test Code
if __name__ == '__main__':
    delData(2)
