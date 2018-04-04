class Item:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


class MovableItem(Item):
    def __init__(self, name):
        super().__init__(name)
        self._lifted = False

    def is_lifted(self):
        return self._lifted

    def lift_item(self):
        self._lifted = True

    def release_item(self):
        self._lifted = False


class UsableItem(MovableItem):
    def __init__(self, name, action):
        super().__init__(name)
        self._action = action

    def get_action(self):
        return self._action
