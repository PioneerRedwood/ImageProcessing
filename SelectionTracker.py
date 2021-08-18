from collections import deque
from tkinter import *

class Selection:
    id = 0
    content = ''

    def __init__(self, id, content):
        self.id = id
        self.content = content

    def __str__(self):
        return self.content


class SelectionTracker:
    selections = 0
    stored = deque()

    root = Tk()
    root.title('tkinter')

    def __init__(self):
        print()

    
    def add(self, str):
        self.selections += 1
        self.stored.append(Selection(self.selections+1, str))
    
    def remove(self):
        self.stored.pop();

    def show(self):
        print('show what have been stored')
        for str in self.stored:
            print(str)

    def save(self):
        print('save as a text file')