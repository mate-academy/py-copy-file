def copy_file(command: str) -> None:
    command_words = command.split(" ")

    if len(command_words) != 3 or command_words[0] != "cp":
        raise ValueError(f"{command} is invalid. Use 'cp source destination'")

    command_name, file_in_path, file_out_path = command_words

    if file_in_path != file_out_path:
        with (
            open(file_in_path, "r") as file_in,
            open(file_out_path, "w") as file_out
        ):
            for line in file_in:
                file_out.write(line)
