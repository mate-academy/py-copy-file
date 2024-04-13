def copy_file(command: str) -> None:
    command_list = command.split()
    if command_list[0] == "cp" and command_list[1] != command_list[2]:
        with (open(command_list[1], "r") as source_file,
              open(command_list[2], "w") as file_copy):
            file_copy.write(source_file.read())
            print("The file successfully copied.")
    else:
        print("Wrong command")
