def copy_file(command: str) -> None:
    names = command.split()
    cd_type, first_file, copys_file = names
    if len(names) == 3 and cd_type == "cd" and not first_file == copys_file:
        with (open(first_file, "r") as file_in,
              open(copys_file, "w") as file_out):
            file_out.write(file_in.read())
