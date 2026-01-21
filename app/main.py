def copy_file(command_line: str) -> None:
    command_list = command_line.split()

    if (
        len(command_list) < 3
        or command_list[0] != "cp"
    ):
        return

    command, path_from, path_to = command_list

    if path_from != path_to:
        try:
            with (
                open(path_from, "r") as file_from,
                open(path_to, "w") as file_to
            ):
                content = file_from.read()
                file_to.write(content)
        except FileNotFoundError as e:
            print(f"Error occurred: {e}")

    return
