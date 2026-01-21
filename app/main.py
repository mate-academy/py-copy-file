def copy_file(command: str) -> None:
    command_list = command.split()
    command_name = command_list[0]
    file_1 = command_list[1]
    file_2 = command_list[2]

    if file_1 != file_2 and command_name == "cp":
        with open(file_1, "r") as file_out, open(file_2, "a") as file_in:
            for copy_line in file_out.readlines():
                file_in.write(f"{copy_line}\n")
