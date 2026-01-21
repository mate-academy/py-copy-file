def copy_file(command: str) -> None:
    command, or_file, new_file = command.split()
    if command == "cp" and or_file != new_file:
        with open(or_file, "r") as file_in, open(new_file, "w") as file_out:
            information = file_in.read()
            file_out.write(information)
