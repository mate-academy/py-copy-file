def copy_file(command: str):
    if command.split()[1] != command.split()[2]:
        with open(f"{command.split()[1]}", "r") as file_in:
            content = file_in.read()
        with open(f"{command.split()[2]}", "w") as file_out:
            file_out.write(f"{content}")
