class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

rect = Rectangle(length=10, width=5)

print("Output when iterating over the Rectangle instance:")
for item in rect:
    print(item)



