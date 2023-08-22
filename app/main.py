def copy_file(command: str):
    command_ls = command.split()
    command_name = command_ls[0]
    current_file = command_ls[1]
    new_file = command_ls[2]

    assert command_name == "cp", f"Command:'{command_name}' is not found"

    if current_file != new_file:
        with open(current_file, "r") as f:
            with open(new_file, "w") as f2:
                f2.write(f.read())

                print(f"File:{current_file} copied!")
