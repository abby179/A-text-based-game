class Room:
    def __init__(self, name):
        self._name = name
        self._items = {}
        self._doors = {}

    def get_name(self):
        return self._name

    def list_items(self):
        return self._items.keys()

    def add_item(self, item, name):
        self._items[name] = item

    def has_item(self, name):
        return name in self._items

    def get_item(self, name):
        return self._items[name]

    def take_item(self, name):
        item = self._items[name]
        item.lift_item()
        print('You took {}'.format(name))
        del self._items[name]

    def set_door(self, direction, door):
        self._doors[direction] = door

    def has_direction(self, direction):
        return direction in self._doors

    def get_door(self, direction):
        return self._doors[direction]

    def get_directions(self):
        return self._doors.keys()

