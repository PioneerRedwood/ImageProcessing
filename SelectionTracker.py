from collections import deque

class SelectionTracker:
    stored = deque()

    def __init__(self):
        print()
    
    def add(self, str):
        self.stored.append(str)
    
    def remove(self):
        self.stored.pop();

    def show(self):
        print('show what have been stored')
        for str in self.stored:
            print(str)

    def save(self):
        print('save as a text file')