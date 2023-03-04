def copy_file(command: str) -> None:
    split_command = command.split()
    input_command, source_file_path, destination_file_path = split_command

    if (len(split_command) == 3
            and input_command == "cp"
            and source_file_path != destination_file_path):
        with open(source_file_path, "r") as file_in, open(
                destination_file_path, "w") as file_out:
            file_out.write(file_in.read())
