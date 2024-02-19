def copy_file(command: str) -> None:
    with open(command.split()[1], "r") as origin_file:
        origin_data = origin_file.read()
    with open(command.split()[2], "r") as copy_file:
        copy_data = copy_file.read()
    if origin_data != copy_data:
        with open(command.split()[2], "w") as file_for_write:
            file_for_write.write(origin_data)
