def copy_file(command: str) -> None:
    files_name = command.split(" ")
    if files_name[1] == files_name[2]:
        return

    with (open(files_name[1], "r") as file_in,
          open(files_name[2], "w") as files_name[2]):
        text = file_in.read()
        files_name[2].write(text)
