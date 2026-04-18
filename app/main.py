def copy_file(command: str) -> bool:

    parts = command.split()

    if len(parts) != 3:
        return False

    if parts[0] != "cp":
        return False

    first_file = parts[1]
    second_file = parts[2]

    if first_file == second_file:
        return False

    try:
        with (open(first_file, "r") as file_in,
              open(second_file, "w") as file_out):
            file_out.write(file_in.read())
            return True
    except FileNotFoundError:
        return False
