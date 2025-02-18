def copy_file(command: str) -> None:
    file_names = command.split()

    if len(file_names) != 3 or file_names[0] != "cp":
        print(
            "Error: The command must include exactly three arguments."
        )
        return

    if file_names[1] == file_names[2]:
        return

    with (
        open(file_names[1], "r") as file_in,
        open(file_names[2], "w") as file_out
    ):
        content = file_in.read()
        file_out.write(content)
