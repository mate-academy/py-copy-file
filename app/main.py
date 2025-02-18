def copy_file(command: str) -> None:
    split_list = command.split(" ")

    file_to_copy = split_list[1]
    new_file = split_list[2]

    if file_to_copy != new_file:
        with (
            open(file_to_copy, "r") as file_in,
            open(new_file, "w") as file_out
        ):
            for line in file_in:
                file_out.write(line)
