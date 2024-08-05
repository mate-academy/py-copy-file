def copy_file(command: str) -> None:
    list_command = command.split()
    name_firs_file = list_command[1]
    name_copy_file = list_command[2]

    if name_firs_file != name_copy_file:
        with (
            open(
                f"{command.split()[1]}",
                "r"
            ) as first_file,
            open(
                f"{command.split()[2]}",
                "w"
            ) as copy_file
        ):
            copy_file.write(first_file.read())
