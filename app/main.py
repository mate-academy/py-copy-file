def copy_file(command: str) -> None:
    if command.split()[0] == "cp":

        with open(f"{command.split()[1]}", "r") as file,\
                open(f"{command.split()[2]}", "a") as file_copy:

            if file.name != file_copy.name:
                file_copy.write(f"{file.read()}")
