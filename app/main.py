import shutil


def copy_file(command: str) -> None:
    command = command.split(" ")
    if len(command) == 3 and command[0] == "cp":
        with (
            open(command[1], "r") as read_file,
            open(command[2], "w") as write_file
        ):
            for line in read_file.readlines():
                write_file.write(line)
        return
    print("Invalid command")
    return

copy_file("cp 1.txt 2.txt")