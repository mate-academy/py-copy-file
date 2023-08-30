def copy_file(command: str) -> None:

    parts = command.split()

    if len(parts) == 3 and parts[0] == "cp":
        cd, file_name, new_file = parts

        if file_name == new_file:
            return

        with open(file_name, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
