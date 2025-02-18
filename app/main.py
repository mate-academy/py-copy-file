def copy_file(command: str) -> None:
    if len(command) != 0:
        cp, old_name, new_name = command.split()
        if old_name != new_name and cp == "cp":
            with open(old_name, "r") as file_in:
                with open(new_name, "w") as file_out:
                    file_out.write(file_in.read())
