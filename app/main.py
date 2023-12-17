def copy_file(command: str) -> None:
    arr_command = command.split()

    if (len(arr_command) != 3
            or arr_command[0] != "cp"
            or arr_command[1] == arr_command[2]):
        return

    with (open(arr_command[1], "r") as file_in,
          open(arr_command[2], "w") as file_out):
        file_out.write(file_in.read())
