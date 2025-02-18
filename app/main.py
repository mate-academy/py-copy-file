def copy_file(command: str) -> None:
    command_parts = command.split()
    if (
        len(command_parts) != 3
        or command_parts[1] == command_parts[2]
        or command_parts[0] != "cp"
    ):
        return

    with open(command_parts[1], "r") as current_file, open(
        command_parts[2], "w"
    ) as new_file:
        new_file.write(current_file.read())


if __name__ == "__main__":
    pass
