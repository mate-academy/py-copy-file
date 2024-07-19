def copy_file(command: str) -> None:
    file, new_file = command.split()[1:3]
    if file == new_file:
        return

    with open(file, "r") as file_in, open(new_file, "w") as file_out:
        for line in file_in:
            file_out.write(line)
