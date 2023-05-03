def copy_file(command: str) -> None:
    new_list = command.split()
    file_needs_copy = new_list[1]
    new_copy_of_file = new_list[2]
    if file_needs_copy == new_copy_of_file:
        return
    with (
        open(file_needs_copy, "r") as file_1,
        open(new_copy_of_file, "w") as file_2
    ):
        file_2.write(file_1.read())
