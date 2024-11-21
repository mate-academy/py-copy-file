def copy_file(command: str) -> None:
    file_in_name = command.split(" ")[1]
    file_out_name = command.split(" ")[2]

    if file_in_name == file_out_name:
        return

    with open(file_in_name) as file_in, open(file_out_name, "w") as file_out:
        file_out.write(file_in.read())
