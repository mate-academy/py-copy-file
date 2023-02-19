def copy_file(command: str) -> None:
    if "cp" not in command:
        return
    files = command.split(" ")
    copied = files[1]
    file_to_copy = files[2]
    if copied == file_to_copy:
        return
    with open(copied, "r") as file_in, open(file_to_copy, "w") as file_out:
        for line in file_in:
            file_out.write(line)
