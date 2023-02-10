def copy_file(command: str) -> None:
    cp, old_name, new_name = command.split()
    if len(cp) != 0:
        if old_name != new_name:
            with open(old_name, "r") as file_out,\
                    open(new_name, "w") as file_in:
                file_in.write(file_out.read())
