def copy_file(command: str) -> None:
    files = command.split(" ")
    old_file = files[1]
    new_file = files[2]

    if old_file != new_file:
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            new_file = file_out.write(file_in.read())
