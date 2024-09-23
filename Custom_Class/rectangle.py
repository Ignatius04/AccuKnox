class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    # Define __iter__ to make this class iterable
    def __iter__(self):
        # Yield the length first in the required format
        yield {'length': self.length}
        # Then yield the width in the required format
        yield {'width': self.width}

# Create an instance of the Rectangle class
rect = Rectangle(10, 5)

# Iterate over the instance and print the values
for dimension in rect:
    print(dimension)
