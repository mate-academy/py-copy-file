def copy_file(command: str) -> None:
    try:
        command, first_part, second_part = command.split()
    except ValueError:
        return

    if first_part == second_part or command != "cp":
        return

    with open(first_part, "r") as file_in, open(second_part, "w") as file_out:
        file_out.write(file_in.read())
