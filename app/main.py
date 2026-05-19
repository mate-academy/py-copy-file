def copy_file(command: str) -> None:
    if not command:
        return
    file_list = command.split()
    if len(file_list) < 3:
        return
    if file_list[0] != "cp":
        return
    try:
        if file_list[1] != file_list[2]:
            with (open(file_list[1], "r") as file_in,
                  open(file_list[2], "w") as file_out):
                file_out.write(file_in.read())
    except FileNotFoundError:
        return
