def copy_file(command: str) -> None:

    command_split = command.split()
    
    if len(command_split) == 3:
        file_command = command_split[0]
        original = command_split[1]
        copy = command_split[2]

        if (original != copy) and (file_command == "cp"):
            with (
                open(original, "r") as original,
                open(copy, "a") as for_copy
            ):
                all_content = original.read()
                for_copy.write(all_content)
