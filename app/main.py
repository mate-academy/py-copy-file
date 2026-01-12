
def copy_file(command: str) -> None:
    arr_command = command.split(" ")

    if len(arr_command) != 3:
        return

    current_file = arr_command[1]
    new_file = arr_command[2]

    if arr_command[0] != "cp":
        return

    if current_file == new_file:
        return

    try:
        with open(current_file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return

