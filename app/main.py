def copy_file(command: str) -> None:
    name_file = command.split()
    if len(name_file) == 3 and name_file[0] == "cp":
        if name_file[1] != name_file[2]:
            with (
                open(name_file[1], "r") as file_in,
                open(name_file[2], "w") as file_out
            ):
                file_out.write(file_in.read())
