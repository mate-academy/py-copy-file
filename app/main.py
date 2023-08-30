def copy_file(command: str) -> None:

    cd, file_name, new_file = command.split(" ")

    if file_name == new_file:
        return
    else:
        with open(file_name, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
