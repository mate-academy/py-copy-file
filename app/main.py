def copy_file(command: str) -> None:
    name_comand, original_file, new_file = command.split()

    if original_file != new_file:
        with open(original_file, "r") as file_get, \
                open(new_file, "w") as file_write:
            info = file_get.read()
            file_write.write(info)
