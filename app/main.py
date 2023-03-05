def copy_file(command: str) -> None:
    old_file = command.split(" ")[1]
    new_file = command.split(" ")[2]
    if old_file == new_file:
        pass
    else:
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
