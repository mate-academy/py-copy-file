def copy_file(command: str):
    command_spl = command.split()
    if command_spl[0] == "cp":
        if command_spl[1] != command_spl[2]:
            with open(command_spl[1], "r") as file1:
                file1 = file1.read()
            with open(command_spl[2], "w") as file2:
                file2.write(file1)
