def copy_file(command: str):
    file = command.split(" ")[1]
    new_file = command.split(" ")[2]
    if file == new_file:
        return None
    with open(f"{file}", "r") as file_in, open(f"{new_file}", "w") as file_out:
        file_out.write(f"{file_in.read()}")
