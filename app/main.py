def copy_file(command: str) -> None:

    command_split = command.split()

    file_original = command_split[1]
    file_for_copy = command_split[2]

    if file_original != file_for_copy:
        with (
            open(file_original, "r") as original,
            open(file_for_copy, "a") as for_copy
        ):
            all_content = original.read()
            for_copy.write(all_content)
