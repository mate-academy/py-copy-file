def copy_file(command: str) -> None:
    splited_data = command.split()
    if len(splited_data) < 3 or splited_data[0] != "cp":
        return
    cmd, first_file, second_file = splited_data
    if first_file != second_file:
        try:
            with (open(first_file, "r") as file_read,
                  open(second_file, "w") as file_write):
                file_write.write(file_read.read())
        except FileNotFoundError:
            return
