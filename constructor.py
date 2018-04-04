import re
from room import Room
from door import Door
from item import *


class Constructor:
    @staticmethod
    def construct_from(file):
        rooms = {}
        with open(file, 'r') as f:
            for line in f:
                if not re.search('^\s|^#', line):
                    tokens = line.strip().split(' ')
                    if tokens[0] == 'room':
                        room_name = tokens[1]
                        rooms[room_name] = Room(room_name)
                    elif tokens[0] == 'door':
                        dirs, status, room1_name, room2_name = tokens[1:]
                        dir1, dir2 = dirs.split('-')
                        room1 = rooms[room1_name]
                        room2 = rooms[room2_name]
                        door = Door(status)
                        door.set_connect(dir1, room2)
                        door.set_connect(dir2, room1)
                        rooms[room1_name].set_door(dir1, door)
                        rooms[room2_name].set_door(dir2, door)
                    elif tokens[0] == 'item':
                        category = tokens[3]
                        item_name = tokens[1]
                        if category == 'STATIONARY':
                            item = Item(item_name)
                        elif category == 'MOVE':
                            item = MovableItem(item_name)
                        else:
                            item = UsableItem(item_name, tokens[4])
                        rooms[tokens[2]].add_item(item, item_name)
                    else:
                        rooms['start'] = rooms[tokens[1]]
        return rooms
