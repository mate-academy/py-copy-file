def copy_file(command: str) -> None:
    standard_copy_command = "cp"
    copy_command_words_total = 3
    copy_command_error_message = "Bad Command"

    normalized_command = command.split()

    if (len(normalized_command) != copy_command_words_total or
            normalized_command[0] != standard_copy_command):
        raise Exception(copy_command_error_message)

    file_to_copy_path, destination_path = normalized_command[1:]

    if file_to_copy_path == destination_path:
        return

    with (open(file_to_copy_path, "r") as file_in,
          open(destination_path, "w") as file_out):
        file_out.write(file_in.read())
