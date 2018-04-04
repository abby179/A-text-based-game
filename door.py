class Door:
    def __init__(self, status):
        self.status = status
        self.room_connect = {}

    def set_connect(self, direction, room):
        self.room_connect[direction] = room

    def open(self):
        if self.status == 'closed':
            self.status = 'open'
            print('Opened the door')
        elif self.status == 'open':
            print('Door already opened')
        elif self.status == 'locked':
            print('Door locked, please first unlock the door')

    def close(self):
        if self.status == 'open':
            self.status = 'closed'
            print('Closed the door')
        elif self.status == 'closed':
            print('Door is already closed')
        elif self.status == 'locked':
            print('Door is already closed and locked')

    def lock(self):
        if self.status == 'closed':
            self.status = 'locked'
            print('Locked the door')
        elif self.status == 'locked':
            print('Door is already locked')
        elif self.status == 'open':
            print('Door is open, please first closed the door')

    def unlock(self):
        if self.status == 'locked':
            self.status = 'closed'
            print('Unlock the door')
        elif self.status == 'closed':
            print('Door is already unlocked')
        elif self.status == 'open':
            print('Door is already open')
