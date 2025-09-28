def copy_file(command: str) -> None:
    try:
        cp, file_copy, file_copied = command.split(" ")
    except ValueError:
        return
    if cp != "cp":
        return
    try:
        if file_copy != file_copied:
            with (open(file_copy, "r") as file_in,
                  open(file_copied, "w+") as file_out):
                content = file_in.read()
                file_out.write(content)
    except FileNotFoundError:
        return
    return
