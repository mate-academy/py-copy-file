def copy_file(command: str) -> None:
    command_elements = command.strip().split(" ")

    if (
        (len(command_elements) == 3
            and command_elements[0] == "cp")
            and command_elements[1] != command_elements[2]
    ):
        try:
            with (
                open(command_elements[1], "r") as file_from,
                open(command_elements[2], "w") as file_to
            ):
                content = file_from.read()
                file_to.write(content)
        except FileNotFoundError:
            print(f"File {command_elements[1]} not found.")
