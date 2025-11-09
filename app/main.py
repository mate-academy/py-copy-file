def copy_file(command: str) -> None:
    if command == "":
        return
    command_list = command.strip().split()
    if len(command_list) != 3 or command_list[0] != "cp":
        return

    try:
        source_file_name = command_list[1]
        destinition_file_name = command_list[2]
        if source_file_name == destinition_file_name:
            return

        with (open(source_file_name, "r") as file_to_copy,
              open(destinition_file_name, "w") as file_to_insert):
            file_to_copy_content = file_to_copy.read()
            file_to_insert.write(file_to_copy_content)
    except FileNotFoundError:
        return FileNotFoundError
    except IndexError:
        return IndexError
