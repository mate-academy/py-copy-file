def copy_file(command: str) -> None:
    files_list = command.split(" ")
    if len(files_list) == 3:
        if files_list[1] != files_list[2]:
            with (open(files_list[1], "r") as file_in,
                  open(files_list[2], "w") as file_out):
                file_out.write(file_in.read())
