def copy_file(command: str) -> None:
    command_parts = command.split(" ")

    if len(command_parts) < 3 or command_parts[0] != "cp":
        raise ValueError(
            "Invalid command format. ""Expected 'cp file copy_file'."
        )

    file, copy_file = command_parts[1], command_parts[2]

    if file != copy_file:
        with open(file, "r") as f, open(copy_file, "w") as fc:
            fc.write(f.read())
