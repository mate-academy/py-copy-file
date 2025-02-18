def copy_file(command: str) -> None:
    command_key_word, file_in_name, file_out_name = command.split()
    if command_key_word == "cp" and file_in_name != file_out_name:
        with (
            open(file_in_name, "r") as file_in,
            open(file_out_name, "w") as file_out
        ):
            file_out.write(file_in.read())
