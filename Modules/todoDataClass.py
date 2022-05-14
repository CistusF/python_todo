# import Module
from datetime import datetime

# Class declaration
class todoData:
    def __init__(self, topic, description="No description.", index=None):
        self.date = datetime.today().strftime("%Y-%m-%d")
        self.topic = topic
        self.description = description
        self.succeeded = False
        self.index = index
    
    def success(self):
        '''Change the success or failure of todo data.'''
        self.succeeded = True

# Test Code
if __name__ == "__main__":
    data = todoData("Update this code.", "When will this code be finished..?")
    print(data.today)
    print(data.succeeded)
    data.success()
    print(data.succeeded)