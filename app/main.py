def copy_file(command: str) -> None:
    command_parts = command.split(" ")

    if not command_parts[0] or command_parts[0] != "cp":
        return

    if command_parts[1] == command_parts[2]:
        return

    with open(command_parts[1], "r") as file_in, open(
            command_parts[2], "w") as file_out:
        content = file_in.read()

        file_out.write(content)
