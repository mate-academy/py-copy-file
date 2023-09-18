def copy_file(command: str) -> None:
    cmd = command.split(" ")
    file_name = cmd[1]
    new_file_name = cmd[2]
    print(new_file_name)
    if file_name != new_file_name:
        with open(f"{file_name}", "r") as file_read:
            read_text = file_read.read()
        with open(f"{new_file_name}", "a") as file_edit:
            file_edit.write(read_text)
    else:
        pass


# copy_file() запуск функции
