def copy_file(command: str) -> None:
    command_elements = command.split()
    _command = command_elements[0]
    if len(command_elements) != 3 or _command != "cp":
        raise ValueError('"command" must be a string with command "cp", '
                         "file name to copy and new file name, "
                         "separated by spaces.")

    file_to_copy, file_to_write = command_elements[1:]
    if (file_to_copy != file_to_write):
        with (open(file_to_copy, "r") as f_to_copy,
              open(file_to_write, "w") as f_to_write):
            f_to_write.write(f_to_copy.read())
