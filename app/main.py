def copy_file(command: str) -> None:
    command_list = command.split()
    cp = command_list[0]
    source_file = command_list[1]
    dest_file = command_list[2]

    if source_file != dest_file and len(command_list) == 3 and cp == "cp":
        with open(source_file, "r") as file1, open(dest_file, "w") as fin_file:
            fin_file.write(file1.read())
