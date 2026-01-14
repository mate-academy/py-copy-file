# write your code here
import os


def copy_file(command: str) -> None:
    splited = command.split(" ")
    if (len(splited) != 3 or splited[0] != "cp"
            or splited[1] == splited[2] or not os.path.isfile(splited[1])):
        return

    source = splited[1]
    destination = splited[2]
    with open(source, "r") as f, open(destination, "w") as f1:
        f1.write(f.read())
