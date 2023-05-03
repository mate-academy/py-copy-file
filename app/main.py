def copy_file(command: str) -> None:
    new_list = command.split()
    if new_list[1] == new_list[2]:
        return
    with (
        open(new_list[1], "r") as file_need_to_copy,
        open(new_list[2], "w") as copied_file
    ):
        copied_file.write(file_need_to_copy.read())
