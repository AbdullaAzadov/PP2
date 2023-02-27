class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, w, h):
        self.x+= w
        self.y+= h
    
    def dist(self, x, y):
        print(abs(self.x - x), abs(self.y - y))

    def show(self):
        print(self.x, self.y)

point = Point(int(input()), int(input()))
point.show()
point.move(int(input()), int(input()))
point.show()
point.dist(int(input()), int(input()))
