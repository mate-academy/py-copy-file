def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        raise ValueError("Command can take only 2 arguments")
    cp_command, file, new_file = command.split()
    if cp_command != "cp":
        raise ValueError("Command not found")

    if file != new_file:
        with open(file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
