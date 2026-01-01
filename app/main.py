def copy_file(command: str) -> None:
    try:
        command_parts = command.split(" ")
        if (
            len(command_parts) != 3
            or not command_parts[0] == "cp"
            or command_parts[1] == command_parts[2]
        ):
            return

        with (
            open(command_parts[1], "r") as file_in,
            open(command_parts[2], "w") as file_out,
        ):
            file_out.write(file_in.read())

    except Exception:
        return
