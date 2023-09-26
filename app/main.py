def copy_file(command: str) -> None:
    splitted_command = command.split()

    terms = (
        len(splitted_command) == 3,
        splitted_command[0] == "cp",
        splitted_command[1] != splitted_command[2]
    )

    if all(terms):
        with open(splitted_command[1], "r") as file_in, open(
            splitted_command[2], "w"
        ) as file_out:
            file_out.write(str(file_in.read()))
