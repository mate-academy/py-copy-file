def copy_file(command: str) -> None:
    command_list = command.split(" ")
    first_file, second_file = command_list[1], command_list[2]

    if first_file != second_file:
        with (open(first_file, "r") as file_from,
              open(second_file, "w") as file_to):
            file_to.write(file_from.read())
