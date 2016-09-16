import attr


@attr.s
class Color(object):
    red = attr.ib()
    green = attr.ib()
    blue = attr.ib()

    def __iter__(self):
        return self.red, self.green, self.blue

    def __getitem__(self, item):
        return (self.red, self.green, self.blue)[item]

    def __len__(self):
        return 3


RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
