def copy_file(command: str):
    command = command.split()
    command_values = {
        "mode": command[0],
        "file": command[1],
        "file_copy": command[2]
    }

    if command_values["mode"] != "cp":
        raise Exception("You need to use command 'cp' to copy file")

    if command_values["file"] != command_values["file_copy"]:
        with open(command_values["file"], "r") as file:
            with open(command_values["file_copy"], "w") as file_copy:
                for line in file:
                    file_copy.write(line)
