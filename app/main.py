def copy_file(command: str):
    command_ls = command.split()

    assert command_ls[0] == "cp", f"Command:'{command_ls[0]}' is not found"

    if command_ls[1] != command_ls[2]:
        with open(command_ls[1], "r") as f:
            with open(command_ls[2], "w") as f2:
                f2.write(f.read())

                print(f"File:{command_ls[1]} copied!")
