def copy_file(command: str) -> None:
    command = command.split()
    if len(command) != 3:
        raise IndexError("Your command is wrong")
    cmd, source_file, destination_file = command
    if source_file == destination_file or cmd == "cp":
        return
    if command[0] == "cp":
        with (
            open(source_file, "r") as source,
            open(destination_file, "w") as destination
        ):
            destination.write(source.read())


if __name__ == "__main__":
    copy_file("cp file.txt new_file.txt")
