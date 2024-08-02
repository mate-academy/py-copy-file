def copy_file(command: str) -> None:
    command_key_word, file_in_name, file_out_name = command.split()
    if command_key_word != "cp" or file_in_name == file_out_name:
        return

    with (
        open(file_in_name, "r") as file_in,
        open(file_out_name, "w") as file_out
    ):
        content_to_copy = file_in.read()
        file_out.write(content_to_copy)
