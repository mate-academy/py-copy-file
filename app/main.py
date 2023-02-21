def copy_file(command: str) -> None:
    _, copied, file_to_copy = command.split(" ")
    if copied == file_to_copy or _ != "cp":
        return
    with open(copied, "r") as file_in, open(file_to_copy, "w") as file_out:
        for line in file_in:
            file_out.write(line)
