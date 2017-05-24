class Collection(object):

    def __init__(self):
        self.items = []
        self.current = 0

    def add(self, item = []):
        self.items.append(item)
        return self

    def items(self):
        return self.items

    def first(self):
        return self.items[0]

    def last(self):
        return self.items[ len(self.items) - 1 ]

    def next(self):
        self.current += 1
        return self.items[ self.current ]

    def prev(self):
        self.current -= 1
        return self.items[ self.current ]
