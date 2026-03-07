from os import path


def copy_file(command: str) -> None:
    keywords_in_command = command.split(" ")
    if len(keywords_in_command) != 3 or keywords_in_command[0] != "cp":
        return
    cmd, file_input, file_output = keywords_in_command
    if path.exists(file_input) and file_input != file_output:
        with (
            open(file_input, "r") as source_file,
            open(file_output, "w") as destination_file
        ):
            destination_file.write(source_file.read())
