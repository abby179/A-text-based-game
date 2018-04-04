import sys
from constructor import Constructor
from runner import Runner


if __name__ == "__main__":
    file = sys.argv[1]
    rooms = Constructor.construct_from(file)
    runner = Runner(rooms)
    runner.run()
