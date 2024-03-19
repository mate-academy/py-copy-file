def copy_file(command: str) -> None:
    key_word, read_file, write_file, *_ = command.split()
    """# After use "*_" instruction no need "len == 3" verif,
    because all the extra parts end up in a variable _ """

    if key_word == "cp" and read_file != write_file:
        with (
            open(read_file, "r") as file_in,
            open(write_file, "w") as file_out
        ):
            file_out.write(file_in.read())
