def copy_file(command: str) -> None:
    cp, file_name, new_file_name = command.split()
    if cp == "cp" and file_name != new_file_name:
        with (
            open(file_name, "r") as file_in,
            open(new_file_name, "w") as file_out
        ):
            content = file_in.read()
            file_out.write(content)
