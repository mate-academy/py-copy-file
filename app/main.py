def copy_file(command: str) -> None:
    data = command.split()
    file_to_copy = data[1]
    copy = data[2]

    if len(data) != 3 or data[0] != "cp" or file_to_copy == copy:
        return

    with open(file_to_copy, "r") as file_in, open(copy, "w") as file_out:
        content = file_in.read()
        file_out.write(content)
