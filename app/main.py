def copy_file(command: str) -> None:
    command_split = command.split()
    if command_split[0] == "cp":
        if command_split[1] == "file.txt":
            with (open("file.txt", "r") as file_in,
                  open("new_file.txt", "w") as file_out):
                content = file_in.read()
                if command_split[2] == "new_file.txt":
                    file_out.write(content)
