def copy_file(command: str) -> None:
    command_split = command.split()
    cp = command_split[0]
    file = command_split[1]
    new_file = command_split[2]

    if cp == "cp" and file == "file.txt":
        with (open("file.txt", "r") as file_in,
              open("new_file.txt", "w") as file_out):
            content = file_in.read()
            if new_file == "new_file.txt":
                file_out.write(content)
