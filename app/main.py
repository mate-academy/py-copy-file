def copy_file(command: str) -> None:
    new_list = command.split(" ")
    if len(new_list) == 3 and new_list[0] == "cp":
        try:
            if new_list[1] != new_list[2]:
                with (open(new_list[1], "r") as file_in,
                      open(new_list[2], "w") as file_out):
                    file_out.write(file_in.read())
        except (IndexError, FileNotFoundError):
            pass
