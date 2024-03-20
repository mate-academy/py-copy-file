def copy_file(command: str) -> None:

    command_list = command.split()

    if len(command_list) != 3:
        raise ValueError(f"Expected 3 arguements, {len(command_list)} "
                         f"were given!")
    if command_list[0] != "cp":
        raise ValueError(f"Expected 'cp' as the first argument, "
                         f"{command_list[0]} was given!")

    file_orig_name = command_list[1]
    file_copy_name = command_list[2]

    if file_orig_name != file_copy_name:
        with (open(file_orig_name, "r") as orig_f,
              open(file_copy_name, "w") as copy_f):
            copy_f.write(orig_f.read())
