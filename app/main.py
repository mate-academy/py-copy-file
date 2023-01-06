def copy_file(command: str) -> None:
    name_list = command.split(" ")
    if name_list[1] != name_list[2]:
        with open(name_list[1], "r") as file_get:
            info = file_get.read()
        with open(name_list[2], "w") as file_write:
            file_write.write(info)
