def copy_file(command: str) -> None:
    cmd_1 = command.split()
    name_of_old_file = cmd_1[1]
    name_of_new_file = cmd_1[2]
    if name_of_old_file != name_of_new_file:
        with (open(name_of_old_file, "r") as file_in,
              open(name_of_new_file, "w") as file_out
        ):
            file_out.write(file_in.read())
