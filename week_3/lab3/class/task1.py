class string():
    def __init__(self, string):
        self.string = string
        
    def printString(self):
        print(self.string.upper)

string(input()).printString()