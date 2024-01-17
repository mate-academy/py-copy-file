def copy_file(command: str) -> None:

    parts_of_command = command.split()
    if len(parts_of_command) != 3 or parts_of_command[0] != "cp":
        return

    first_file, second_file = parts_of_command[1], parts_of_command[2]

    if first_file == second_file:
        return

    with open(first_file, "r") as file_in, open(second_file, "w") as file_out:
        file_out.write(file_in.read())
