def copy_file(command: str) -> None:
    command = command.split()
    if command[0] == "cp" and command[1] != command[2]:
        with (
                open(command[1], "r") as source_file,
                open(command[2], "w") as result_file
        ):
            result_file.write(source_file.read())
