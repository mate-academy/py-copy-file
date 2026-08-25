def copy_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) != 3 or command_split[0] != "cp":
        return
    file_name_original, file_name_copy = command.split()[1:]
    if file_name_copy == file_name_original:
        return

    try:
        with (open(file_name_original) as file_read,
              open(file_name_copy, "w") as file_write):
            for line in file_read:
                file_write.write(line)
    except FileNotFoundError as e:
        print(e)
