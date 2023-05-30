def copy_file(command: str) -> None:
    command = command.split()
    source_file = command[1]
    destination_file = command[2]
    if command[0] == "cp":
        if len(command) != 3:
            raise IndexError("list index out of range")
        if source_file == destination_file:
            return
        if len(command) == 3:
            with (open(source_file, "r") as file_in,
                open(destination_file, "w") as file_out):
                    file_out.write(file_in.read())


if __name__ == "__main__":
    copy_file(command = __name__)