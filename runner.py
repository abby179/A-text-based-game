from item import *
from player import Player


class Runner:
    def __init__(self, rooms):
        self.current = rooms['start']
        del rooms['start']
        self.rooms = rooms
        self.player = Player()
        self.commands = ['go DIR', 'open DIR', 'close DIR', 'lock DIR', 'unlock DIR', 'take ITEM',
                         'release ITEM', 'read ITEM', 'show', 'commands', 'holding', 'quit']

    def print_current_state(self):
        room_name = self.current.get_name()
        print('You are in the {}.'.format(room_name))
        directions = self.current.get_directions()
        print('There are doors towards {}'.format(', '.join(directions)))
        room_items = self.current.list_items()
        if len(room_items):
            print('Here are the following items:')
            for i in room_items:
                print(i)

    def print_holding(self):
        player_items = self.player.get_items()
        if len(player_items):
            print('You hold following items:')
            for i in player_items:
                print(i)
        else:
            print('You hold nothing')

    def print_commands(self):
        print('There are below commands for you to play:')
        for command in self.commands:
            print(command)

    def run(self):
        print('Welcome to the house game!')
        self.print_current_state()
        command = input('\nPlease type commands in order to play the game!\n> ')
        while command.strip() != 'quit':
            cmd = command.strip().split(' ')
            if cmd[0] == 'go':
                direction = cmd[1]
                if self.current.has_direction(direction):
                    self.go(direction)
                else:
                    print('There is no door to go')
            elif cmd[0] == 'open':
                direction = cmd[1]
                if self.current.has_direction(direction):
                    self.open(direction)
                else:
                    print('There is no door to open')
            elif cmd[0] == 'close':
                direction = cmd[1]
                if self.current.has_direction(direction):
                    self.close(direction)
                else:
                    print('There is no door to close')
            elif cmd[0] == 'lock':
                direction = cmd[1]
                if self.current.has_direction(direction):
                    self.lock(direction)
                else:
                    print('There is no door to lock')
            elif cmd[0] == 'unlock':
                direction = cmd[1]
                if self.current.has_direction(direction):
                    self.unlock(direction)
                else:
                    print('There is no door to unlock')
            elif cmd[0] == 'take':
                item_name = cmd[1]
                if self.current.has_item(item_name):
                    self.take(item_name)
                else:
                    print('There is no item to take')
            elif cmd[0] == 'release':
                item_name = cmd[1]
                if self.player.has_item(item_name):
                    self.release(item_name)
                else:
                    print('There is no item to release')
            elif cmd[0] == 'read':
                item_name = cmd[1]
                if self.player.has_item(item_name):
                    self.read(item_name)
                else:
                    print('There is no item to read')
            elif cmd[0] == 'show':
                self.print_current_state()
            elif cmd[0] == 'holding':
                self.print_holding()
            elif cmd[0] == 'commands':
                self.print_commands()
            else:
                print('I do not understand')
            command = input('> ')
        print('Good bye and thanks for playing!')

    def go(self, direction):
        door = self.current.get_door(direction)
        if door.status == 'open':
            self.current = door.room_connect[direction]
            self.print_current_state()
        elif door.status == 'closed':
            print('The door is closed')
        else:
            print('The door is locked')

    def open(self, direction):
        door = self.current.get_door(direction)
        door.open()

    def close(self, direction):
        door = self.current.get_door(direction)
        door.close()

    def lock(self, direction):
        door = self.current.get_door(direction)
        if self.player.has_item('key'):
            door.lock()
        else:
            print('you must hold a key to lock the door')

    def unlock(self, direction):
        door = self.current.get_door(direction)
        if self.player.has_item('key'):
            door.unlock()
        else:
            print('you must hold a key to unlock the door')

    def take(self, name):
        item = self.current.get_item(name)
        if isinstance(item, MovableItem):
            self.current.take_item(name)
            self.player.lift_item(item, name)
        else:
            print('{} cannot be lifted'.format(name))

    def release(self, item_name):
        item = self.player.release_item(item_name)
        self.current.add_item(item, item_name)

    def read(self, item_name):
        item = self.player.get_item(item_name)
        if isinstance(item, UsableItem):
            if item.get_action() == 'read':
                print('read {}'.format(item.get_name()))
            else:
                print('this item cannot be read')
        else:
            print('this item cannot be used')
