def copy_file(command: str) -> None:
    ls_command = command.split(" ")
    if not (len(ls_command) == 3
            and ls_command[0] == "cp"
            and ls_command[1] != ls_command[2]):
        return

    source_file, dest_file = ls_command[1], ls_command[2]

    try:
        with open(source_file, "r") as file_in, \
                open(dest_file, "w") as file_out:
            file_out.write(file_in.read())

    except FileNotFoundError:
        return
