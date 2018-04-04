class Player:
    def __init__(self):
        self._items = {}

    def get_items(self):
        return self._items.keys()

    def has_item(self, name):
        return name in self._items

    def lift_item(self, item, name):
        self._items[name] = item

    def get_item(self, name):
        return self._items[name]

    def release_item(self, name):
        item = self._items[name]
        item.release_item()
        print('You put {}'.format(name))
        del self._items[name]
        return item
