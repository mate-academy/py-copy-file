def copy_file(command: str) -> None:
    old_file, new_file = command.split(" ")[1:]

    if old_file != new_file:
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
