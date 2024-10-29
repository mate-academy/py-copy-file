# write your code here
import os


def copy_file(command: str):

    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "cp":
        print("Invalid command format")
        return

    source, direction = command_parts[1], command_parts[2]

    if source == direction:
        return

    if not os.path.isfile(source):
        return

    try:
        with open(source, "r") as source, open(direction, "w") as direction:
            direction.write(source.read())
    except (FileNotFoundError, IOError) as err:
        print("Error: ", err)
