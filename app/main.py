def copy_file(command: str) -> None:
    _, file_name, copy_name = command.split(" ")
    if file_name == copy_name:
        return
    with open(file_name, "r") as file_in, open(copy_name, "w") as file_out:
        for line in file_in:
            file_out.write(f"{line}")
