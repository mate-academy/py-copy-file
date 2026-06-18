def copy_file(command: str) -> None:
    files = command.split(" ")

    if len(files) != 3:
        return

    if files[0] != "cp":
        return

    if files[1] == files[2]:
        return

    if files[1] != files[2]:
        try:
            with (open(files[1], "r") as file_in,
                  open(files[2], "w") as file_out):
                file_out.write(file_in.read())
        except FileNotFoundError:
            return
