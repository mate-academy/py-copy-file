def copy_file(command: str) -> None:
    input_command, file_in, file_out = command.split()
    if command == "cp" and file_in != file_out:
        with (
            open(file_in, "r") as file_to_copy,
            open(file_out, "a+") as copy_of_file
        ):
            lines = file_to_copy.readlines()
            for line in lines:
                copy_of_file.write(line)
