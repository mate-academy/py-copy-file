def copy_file(command_files: str) -> None:
    parts = command_files.split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    file_name_1, file_name_2 = parts[1], parts[2]
    if f"{file_name_1}" == f"{file_name_2}":
        return

    try:
        with (open(file_name_1, "r") as file_in,
              open(file_name_2, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        pass
