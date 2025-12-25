def copy_file(command: str) -> None:
    command_list = command.split(" ")
    if len(command_list) == 3:
        command = command_list[0]
        file_to_copy = command_list[1]
        new_file = command_list[2]

        if command == "cp" and file_to_copy != new_file:
            try:
                with open(file_to_copy, mode="r") as file_read:
                    file_data = file_read.readlines()

                with open(new_file, mode="w") as file_write:
                    file_write.write("".join(file_data))
            except FileNotFoundError:
                return
