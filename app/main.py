def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    command_name, source_file, target_file = parts
    if source_file == target_file:
        return
    if command_name != "cp":
        return
    try:
        with (
            open(source_file, "r") as file_in,
            open(target_file, "w") as file_out
        ):
            content = file_in.read()
            file_out.write(content)
    except FileNotFoundError:
        print("Source or destination path does not exist")
