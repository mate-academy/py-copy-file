def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[0] == "cp":
        _, original_file, copied_file = parts
        if original_file != copied_file:
            with (
                open(original_file, "r") as file_in,
                open(copied_file, "w") as file_out
            ):
                file_out.write(file_in.read())
