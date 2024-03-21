def copy_file(command: str) -> None:
    standard_copy_command = "cp"
    copy_command_words_total = 3
    copy_command_error_message = "Bad Command"

    normalized_command = command.split(" ")

    if len(normalized_command) != copy_command_words_total:
        raise Exception(copy_command_error_message)

    copy_command, file_to_copy_path, destination_file_to_copy_path = normalized_command

    if copy_command != standard_copy_command:
        raise Exception(copy_command_error_message)

    if file_to_copy_path == destination_file_to_copy_path:
        return

    with (open(file_to_copy_path, "r") as file_in,
          open(destination_file_to_copy_path, "w") as file_out):
        file_out.write(file_in.read())
