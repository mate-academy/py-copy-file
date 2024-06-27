def copy_file(command: str) -> None:
    command_split = command.split()

    reports_copy = command_split[1]
    where_copy = command_split[2]

    if reports_copy == where_copy:
        return

    with open(reports_copy, "r") as file_in, open(where_copy, "w") as file_out:
        file_out.write(file_in.read())

