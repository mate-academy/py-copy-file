def copy_file(command: str) -> bool | None:
    list_files = command.split(" ")

    if len(list_files) != 3:
        return None

    if list_files[0] != "cp":
        return False

    try:
        with (open(list_files[1], "r") as file_in,
              open(list_files[2], "w") as file_out):
            if list_files[1] != list_files[2]:
                for line in file_in:
                    file_out.write(f"{line}")
    except FileNotFoundError:
        return False
