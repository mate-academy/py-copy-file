def copy_file(command: str) -> None:
    file_list = command.split(" ")

    if file_list[1] == file_list[2]:
        return

    with (open(file_list[1], "r") as file_in,
          open(file_list[2], "w") as file_out):
        file_out.write(file_in.read())
