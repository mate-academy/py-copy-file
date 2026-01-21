def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3:
        return

    command_cli, source_file, target_file = command_parts

    if command_cli != "cp" or source_file == target_file:
        return

    try:
        with (
            open(source_file, "r") as file_in,
            open(target_file, "w") as file_out,
        ):
            content = file_in.read()
            file_out.write(content)
    except FileNotFoundError:
        return
