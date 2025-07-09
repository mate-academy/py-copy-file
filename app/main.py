def copy_file(command: str) -> None:
    name_of_file = command.split(" ")

    if len(name_of_file) != 3 or name_of_file[0] != "cp":
        return

    if name_of_file[1] == name_of_file[2]:
        return

    try:
        with (
            open(name_of_file[1], "r") as file_in,
            open(name_of_file[2], "w") as file_out
        ):
            file_out.write(file_in.read())
    except FileNotFoundError:
        pass
