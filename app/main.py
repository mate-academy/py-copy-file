def copy_file(command: str) -> None:
    command = command.split(" ")
    copy_file = command[1]
    new_file = command[2]
    if copy_file == new_file:
        return

    with (
        open(copy_file) as file_in,
        open(new_file, "w") as file_out
    ):
        file_out.writelines(file_in.readlines())
