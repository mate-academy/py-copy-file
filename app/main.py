def copy_file(command: str) -> None:
    command, first_file, second_file = command.split(" ")
    if first_file == second_file or command != "cp":
        return
    with open(first_file, "r") as file_in, open(second_file, "w") as file_out:
        file_out.write(file_in.read())