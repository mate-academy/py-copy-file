def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        raise ValueError(
            "Command must be in the format: cp source_path dest_path"
        )

    cp, source_path, dest_path = parts

    if cp != "cp":
        raise ValueError("Invalid command. Only 'cp' command is supported.")

    if source_path == dest_path:
        return

    with open(source_path, "r") as file_in, open(dest_path, "w") as file_out:
        content = file_in.read()
        file_out.write(f"{content}")
