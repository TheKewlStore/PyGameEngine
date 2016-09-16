import attr


@attr.s
class Size(object):
    width = attr.ib()
    height = attr.ib()

    def __iter__(self):
        return self.width, self.height

    def __getitem__(self, item):
        return (self.width, self.height)[item]

    def __len__(self):
        return 2
