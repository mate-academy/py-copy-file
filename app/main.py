def copy_file(command: str) -> None:
    command = command.split()
    cp, file_to_copy_name, new_file_name = command

    if cp == "cp" and not file_to_copy_name == new_file_name:
        with (
            open(file_to_copy_name, "r") as file_in,
            open(new_file_name, "w") as file_out
        ):
            text_to_copy = file_in.read()
            file_out.write(text_to_copy)
