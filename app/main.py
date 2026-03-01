def copy_file(command: str) -> None:
    file_names = command.split(" ")
    if len(file_names) != 3:
        return
    if file_names[0] != "cp":
        return
    if file_names[1] == file_names[2]:
        return
    else:
        try:
            with (open(file_names[1], "r") as file_in,
                  open(file_names[2], "w") as file_out):
                content = file_in.read()
                file_out.write(content)
        except FileNotFoundError:
            return
