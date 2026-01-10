def copy_file(command: str) -> None:
    command_name = command.split()

    if len(command_name) != 3:
        return
    if "cp" != command_name[0]:
        return

    first_file = command_name[1]
    second_file = command_name[2]

    if first_file == second_file:
        return
    try:
        with (open(first_file, "r") as file_in,
              open(second_file, "w") as file_out):
            file_out.write(file_in.read())
    except Exception:
        pass
