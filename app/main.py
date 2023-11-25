def copy_file(command: str) -> None:
    command_elements = command.split()
    _command = command_elements[0]
    file_to_copy = command_elements[1]
    file_to_write = command_elements[2]
    if (_command == "cp"
            and len(command_elements) == 3
            and file_to_copy != file_to_write):

        with (open(file_to_copy, "r") as f_to_copy,
              open(file_to_write, "w") as f_to_write):
            f_to_write.write(f_to_copy.read())
