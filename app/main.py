def copy_file(command: str) -> None:
    command_parts = command.split(" ")
    if len(command_parts) != 3:
        return

    cp, source_file_name, target_file_name = command_parts

    if cp != "cp":
        return

    if source_file_name == target_file_name:
        return

    try:
        with (open(source_file_name, "r") as file_in,
              open(target_file_name, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        pass
