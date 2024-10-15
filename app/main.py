def copy_file(command: str) -> None:
    list_ = command.split()
    first_name = str(list_[1])
    second_name = str(list_[2])
    if first_name == second_name:
        return
    with open(first_name, "r") as file_in, open(second_name, "w") as file_out:
        file_out.write(file_in.read())
