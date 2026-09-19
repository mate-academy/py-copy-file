def copy_file(command: str) -> None:
    split_command = command.split(" ")
    if len(split_command) == 3 and split_command[0] == "cp":
        name_of_command, file_name_to_copy, file_name_to_insert = split_command
        if file_name_to_copy == file_name_to_insert:
            return
        try:
            with (open(file_name_to_copy, "r") as copy_file_to,
                  open(file_name_to_insert, "w") as insert_file):
                insert_file.write(copy_file_to.read())
        except FileNotFoundError:
            return
