def copy_file(command: str) -> None:
    words = command.split(" ")
    command_name = words[0]
    name_to_copy = words[1]
    new_file_name = words[2]
    if (
            len(words) != 3
            or command_name != "cp"
            or name_to_copy == new_file_name
    ):
        return None
    with (
        open(name_to_copy, "r") as file_in,
        open(new_file_name, "w") as file_out
    ):
        file_out.write(file_in.read())
