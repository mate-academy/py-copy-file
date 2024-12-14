def copy_file(command: str) -> None:
    if command.split()[0] == "cp" and len(command.split()) == 3:
        try:
            cp, file_name, new_name = command.split()
            if file_name != new_name:
                with (open(file_name, "r") as file_in,
                      open(new_name, "x") as file_out):
                    file_out.write(file_in.read())
        except FileExistsError:
            pass
