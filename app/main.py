def copy_file(command: str) -> None:
    command, file_name, copy_file_name = command.split(" ")

    if command == "cp" and file_name != copy_file_name:
        with (
            open(file_name, "r") as file_in,
            open(copy_file_name, "w") as file_out
        ):
            content = file_in.read()
            file_out.write(content)
