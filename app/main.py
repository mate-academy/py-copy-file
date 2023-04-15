def copy_file(command: str) -> None:
    com, first_file, second_file = command.split()
    if first_file == second_file or com != "cp":
        return
    with open(first_file, "r") as file_in, open(second_file, "w") as file_out:
        file_out.write(file_in.read())


copy_file("cp file.txt new_file.txt")
