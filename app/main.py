def copy_file(command: str) -> None:
    command, file_name, copy_name = command.split()
    if command != "cp":
        print(f"{command}: command not found")
        return
    with open(file_name, "r") as file_in, open(copy_name, "w") as file_out:
        file_out.write(file_in.read())
