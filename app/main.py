def copy_file(command: str) -> None:
    split_command = command.split(" ")

    if len(split_command) == 3:
        if split_command[0] == "cp":
            if split_command[1] != split_command[2]:
                action, file, new_file = split_command

                with open(file) as file_in, open(new_file, "w") as file_out:
                    file_out.write(file_in)
