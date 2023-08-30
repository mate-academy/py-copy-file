def copy_file(command: str) -> None:

    if len(command.split()) == 3 and command.split()[0] == "cp":
        cd, file_name, new_file = command.split()

        if file_name == new_file:
            return

        with open(file_name, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
