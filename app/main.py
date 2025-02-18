def copy_file(command: str) -> None:
    command, old_file, new_file = command.split()
    if new_file != old_file and command == "cp":
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
