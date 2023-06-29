def copy_file(command: str) -> None:
    command = command.split()
    if len(command) != 3:
        raise IndexError("list index out of range")
    source_file = command[1]
    destination_file = command[2]
    if source_file == destination_file:
        return
    if command[0] == "cp":
        with (open(source_file, "r") as f,
                open(destination_file, "w") as s):
            s.write(f.read())


copy_file("cp file.txt new_file.txt")
