class Shape():
    def __init__(self, len):
        self.len = len
        self.a = 0
    def area(self):
        print(self.a)

class Square(Shape):
    def __init__(self, len):
        self.a = len ** 2
    
Square(int(input())).area()