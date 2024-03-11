def copy_file(command: str) -> None:
    names = command.split()
    if len(names) == 3:
        cd_type, first_file, copys_file = names
    else:
        return
    if cd_type == "cp" and not first_file == copys_file:
        with (open(first_file, "r") as file_in,
              open(copys_file, "w") as file_out):
            file_out.write(file_in.read())
