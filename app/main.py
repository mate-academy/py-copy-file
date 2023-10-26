def copy_file(command: str) -> None:

    command_args = command.split()

    if len(command_args) != 3:
        return

    cp, file, file_copy = command_args
    if cp != "cp" or file == file_copy:
        return

    with open(file, "r") as file_in, open(file_copy, "w") as file_out:
        old_file_text = file_in.read()
        file_out.write(old_file_text)
