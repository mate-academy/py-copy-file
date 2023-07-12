def copy_file(command: str) -> None:
    file_split = command.split()
    file_in_name = file_split[1]
    file_out_name = file_split[2]
    if file_in_name != file_out_name:
        with open(file_in_name, "r") as file_in, open(file_out_name, "w") as file_out:
            file_out.write(file_in.read())
