# A-text-based-game
The game is about a player walks around in a house, and can take and use items that are placed in the house. Every thing is initialized with the document "gameConfiguration.txt". The house description file should be given as an argument when starting your game: python3 textGame.py gameConfiguration.txt

You could use below commands:
- go DIR: Let’s the player move to the room in direction DIR, if there is an open door in that direction.
- take ITEM: Let’s the player take the item ITEM if it is in the same room as the player, and ITEM is not a STATIONARY item. The item should then be held by the player, and no longer available in the room.
- release ITEM: Let’s the player release item ITEM, if he holds it. The item will then be in the room the player is in, and should no longer be held by the player.
- open DIR: Opens the door in direction DIR in the current room, if there is such a door, and if that door is closed.
- unlock DIR: requires a key to unlock a door
- lock DIR: requires a key to lock a door
- Read ITEM – reads some hidden text in an item like a book or note, for instance a clue to the player. The text to be displayed can be added to the house description.
- show: Describes the room the player is currently in, i.e. gives its name, lists the doors, and the available items, if any.
- commands: Lists all available commands in the game.
- holding: Lists all the items the player is currently holding.
- quit: Ends the game.
