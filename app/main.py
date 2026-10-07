def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        return
    cp, file_name, copy_file_name = command.split()
    if cp != "cp":
        return
    if file_name == copy_file_name:
        return
    else:
        try:
            with (open(file_name, "r") as file_from,
                  open(copy_file_name, "w") as file_where):
                file_where.write(file_from.read())
        except FileNotFoundError:
            return
