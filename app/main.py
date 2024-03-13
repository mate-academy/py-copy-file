def copy_file(command: str) -> None:
    file_origin = command.split()[1]
    cp_file = command.split()[2]
    if file_origin != cp_file:
        with open(file_origin, "r") as file_in, open(cp_file, "w") as file_out:
            file_out.write(file_in.read())
