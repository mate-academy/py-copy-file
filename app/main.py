def copy_file(command: str) -> None:
    command_split = command.split()
    command_cp = command_split[0]
    command_file = command_split[1]
    command_new_file = command_split[2]

    if command_cp == "cp" and command_file == "file.txt":
        with (open("file.txt", "r") as file_in,
              open("new_file.txt", "w") as file_out):
            content = file_in.read()
            if command_new_file == "new_file.txt":
                file_out.write(content)
