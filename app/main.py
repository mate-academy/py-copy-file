def copy_file(command: str) -> None:
    command = command.split(" ")
    file_to_copy = command[1]
    new_file = command[-1]

    if file_to_copy != new_file:
        with open(file_to_copy, "r") as source, open(new_file, "w") as copy:
            for line in source:
                copy.write(line)
