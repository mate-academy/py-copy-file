def copy_file(command: str) -> None:
    """
    this function designed for copying two files
    :param command: "cp file_to_copy.format new_file.format"
    """
    file_1 = command.split(" ")[1]
    file_2 = command.split(" ")[2]
    with open(file_1, "r") as file_in, open(file_2, "w") as file_out:
        file_out.write(file_in.read())
