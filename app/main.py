def copy_file(command: str) -> None:
    parsed_command = command.split()
    if (
        len(parsed_command) != 3
        or parsed_command[1] == parsed_command[2]
        or parsed_command[0] != "cp"
    ):
        return

    with open(parsed_command[1], "r") as current_file, open(
        parsed_command[2], "w"
    ) as new_file:
        new_file.write(current_file.read())


if __name__ == "__main__":
    copy_file(input("Input command: "))
