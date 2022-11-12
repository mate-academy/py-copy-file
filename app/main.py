def copy_file(command: str) -> None:
    file_name = command.split(" ")[1]
    new_file_name = command.split(" ")[2]
    if file_name == new_file_name:
        return None
    with open(f"{file_name}", "r") as file_in, open(f"{new_file_name}", "w")\
            as file_out:
        file_out.write(f"{file_in.read()}")
