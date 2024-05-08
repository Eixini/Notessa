class TreeItem:
    def __init__(self, data, parent=None):
        self.parent_item = parent
        self.item_data = data
        self.children = []

    def child(self, row):
        return self.children[row]

    def child_count(self):
        return len(self.children)

    def child_number(self):
        if self.parent_item is not None:
            return self.parent_item.children.index(self)

    def column_count(self):
        return len(self.item_data)

    def data(self, column):
        return self.item_data[column]

    def insert_children(self, position, count, columns):
        if position < 0 or position > len(self.children):
            return False
        for row in range(count):
            data = [v for v in range(columns)]
            item = TreeItem(data, self)
            self.children.insert(position, item)

    def parent(self):
        return self.parent_item

    def set_data(self, column, value):
        if column < 0 or column >= len(self.item_data):
            return False
        self.item_data[column] = value
