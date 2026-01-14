def copy_file(command: str) -> None:
    splitted_command = command.split(" ")
    if len(splitted_command) == 3:
        source_file_name = splitted_command[1]
        destination_file_name = splitted_command[2]
        if (source_file_name != destination_file_name
                and splitted_command[0] == "cp"):
            try:
                with (open(source_file_name , "r") as file_in,
                      open(destination_file_name , "w") as file_out):
                    file_out.write(file_in.read())
            except FileNotFoundError:
                return
