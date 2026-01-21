def copy_file(command: str) -> None:
    files = command.split()
    if len(files) != 3 or files[0] != "cp":
        return

    first_file = files[1]
    second_file = files[2]
    if first_file == second_file:
        return

    try:
        with (open(first_file, "r") as file_in,
              open(second_file, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
