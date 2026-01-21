def copy_file(command: str) -> None:
    command_list = command.split()
    if (len(command_list) == 3 and command_list[0] == "cp"
            and command_list[1] != command_list[2]):
        with (open("file.txt", "r") as file_in,
              open("new_file.txt", "w") as file_out):
            file_out.write(file_in.read())
